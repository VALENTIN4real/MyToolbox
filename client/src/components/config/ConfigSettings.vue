<template>
<div class="container">
  <h1>Configurations</h1>
  <div>
    <b-tabs content-class="mt-3">
      <b-tab title="Utilisateurs">
        <div class="d-flex justify-content-between">
          <h2>Utilisateurs</h2>
        </div>
        <div class="d-flex justify-content-end">
          <b-button @click="showModal({})">Ajouter un utilisateur</b-button>


        </div>
      </b-tab>
      <b-tab title="Second"><p>I'm the second tab</p></b-tab>
    </b-tabs>
  </div>
  <CreateEditUserModal v-model="isModalVisible" :dataForm="userForm" />
</div>
</template>

<script>
import axios from 'axios'
import CreateEditUserModal from '@/components/tools/CreateEditUserModal.vue'

export default {
  name: 'ConfigSettings',
  components: { CreateEditUserModal },
  props: {},
  data() {
    return {
      isModalVisible: false,
      userForm: {},
      users: [],
      operations: []
    }
  },
  mounted() {
    this.getUsers()
    this.getOperations()
  },
  methods: {
    showModal(user) {
      console.log("showModal")
      this.userForm = user
      this.isModalVisible = ! this.isModalVisible
    },

    createUser() {
      axios.post(this.$env.API_URL + 'users', this.userForm)
        .then(response => {
          console.log(response.data)
        })
        .catch(err => {
          console.error(err)
        })
    },

    getUsers() {
      console.log('getUsers')
      axios.get(this.$env.API_URL + 'users')
        .then(response => {
          console.log(response.data)
          this.users = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },

    getOperations() {
      console.log('getOperations')
      axios.get(this.$env.API_URL + 'operations')
        .then(res => {
          console.log(res.data)
          this.operations = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
}
</script>

<style>

</style>
