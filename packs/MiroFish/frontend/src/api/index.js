import axios from 'axios'

// Usa VITE_API_BASE_URL si existe; en caso contrario usa la misma origin
// para aprovechar el proxy /api de Vite en despliegues remotos.
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '',
  timeout: 300000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Interceptor de request
service.interceptors.request.use(
  config => {
    return config
  },
  error => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// Interceptor de response
service.interceptors.response.use(
  response => {
    const res = response.data
    
    // Si la API devuelve success=false, propaga error normalizado
    if (!res.success && res.success !== undefined) {
      console.error('API Error:', res.error || res.message || 'Unknown error')
      return Promise.reject(new Error(res.error || res.message || 'Error de API'))
    }
    
    return res
  },
  error => {
    console.error('Response error:', error)
    
    // Timeout
    if (error.code === 'ECONNABORTED' && error.message.includes('timeout')) {
      console.error('Request timeout')
      return Promise.reject(new Error('Tiempo de espera agotado al conectar con el backend.'))
    }
    
    // Error de red (backend caido, URL incorrecta o CORS)
    if (error.message === 'Network Error') {
      console.error('Network error - please check your connection')
      return Promise.reject(new Error('Error de red: no se pudo conectar con el backend.'))
    }
    
    return Promise.reject(error)
  }
)

// Helper con reintento exponencial
export const requestWithRetry = async (requestFn, maxRetries = 3, delay = 1000) => {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await requestFn()
    } catch (error) {
      if (i === maxRetries - 1) throw error
      
      console.warn(`Request failed, retrying (${i + 1}/${maxRetries})...`)
      await new Promise(resolve => setTimeout(resolve, delay * Math.pow(2, i)))
    }
  }
}

export default service
