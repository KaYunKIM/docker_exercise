import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

import SERVER from '@/API/url'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      visitorList: {},
  },

  mutations: {
    SET_VISITORLIST(state, visitorList) {
      state.visitorList = visitorList 
    }
  },

  actions: {
    fetchVisitorList({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.register)
        .then(res => commit('SET_VISITORLIST', res.data))
        .catch(err => console.error(err.response.data))
    },
    
    addVisitor({ dispatch }, visitorInfo){
      console.log('addVisitor ok', visitorInfo)
      axios.post(SERVER.URL + SERVER.ROUTES.register, visitorInfo)
        .then(() => dispatch('fetchVisitorList'))
        .catch(err => console.error(err.response.data))
    }
  }
})