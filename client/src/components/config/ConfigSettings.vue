<template>
<div class="container">
  <h1>Configurations</h1>
  <div>
    <b-tabs content-class="mt-3">
      <b-tab title="Utilisateurs">
        <div class="d-flex justify-content-between">
          <h2>Utilisateurs</h2>
          <b-button @click="showModal({})">Ajouter un utilisateur</b-button>
        </div>
        <div class="d-flex justify-content-end">
          <BTableSimple striped hover>
            <BThead>
              <BTr>
                <BTh>ID</BTh>
                <BTh>Nom</BTh>
                <BTh>TR</BTh>
                <BTh>Montant TR</BTh>
                <BTh>Part salariale</BTh>
                <BTh>Part patronale</BTh>
              </BTr>
            </BThead>
            <BTbody v-if="users.length > 0">
              <BTr v-for="user in users" :key="user.id" @click="showModal(user)">
                <BTd>{{ user.id }}</BTd>
                <BTd>{{ user.name }}</BTd>
                <BTd>{{ user.has_tr ? "Oui" : "Non"}}</BTd>
                <BTd>{{ user.tr_value }} €</BTd>
                <BTd>{{ user.tr_employee_share }} €</BTd>
                <BTd>{{ user.tr_employer_share }} €</BTd>
              </BTr>
            </BTbody>
            <div v-else>Aucun utilisateur trouvé.</div>
          </BTableSimple>
        </div>
      </b-tab>
      <b-tab title="Second"><p>I'm the second tab</p></b-tab>
    </b-tabs>
  </div>
  <CreateEditUserModal v-model="isModalVisible" :dataForm="userForm" @refreshUsers="getUsers"/>

</div>
</template>

<script>
import axios from 'axios'
import CreateEditUserModal from '@/components/users/CreateEditUserModal.vue'

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
      this.isModalVisible = true
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
