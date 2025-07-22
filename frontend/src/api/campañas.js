import api from '../axios'

export function simularCampaña(campaña, usuarios) {
  return api.post('/campañas/simular', { campaña, usuarios })
}
