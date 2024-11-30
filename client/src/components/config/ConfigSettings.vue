<template>
<div class="container">
  <h1>Configurations</h1>
  <BTabs content-class="mt-3 hover" justified>
    <BTab title="Utilisateurs" active>
      <BTableSimple striped hover v-if="Object.keys(users).length > 0" :items="users" >
        <BThead head-variant="dark">
          <BTr>
            <BTh>ID</BTh>
            <BTh>Nom</BTh>
            <BTh>TR</BTh>
            <BTh>Montant TR</BTh>
            <BTh>Part salarié</BTh>
            <BTh>Part employeur</BTh>
          </BTr>
        </BThead>
        <BTbody>
          <BTr v-for="user in users" :key="user.id">
            <BTd>{{ user.id }}</BTd>
            <BTd>{{ user.name }}</BTd>
            <BTd v-if="user.has_tr">Oui</BTd>
            <BTd v-else>Non</BTd>
            <BTd>{{ user.tr_value }} €</BTd>
            <BTd>{{ user.tr_employee_share }} €</BTd>
            <BTd>{{ user.tr_employer_share }} €</BTd>
          </BTr>
        </BTbody>
      </BTableSimple>
      <p v-else>Aucun utilisateur trouvé.</p>
    </BTab>
    <BTab title="Opérations">
      <BTableSimple striped hover v-if="Object.keys(operations).length > 0" :items="operations" >
        <BThead head-variant="dark">
          <BTr>
            <BTh>ID</BTh>
            <BTh>Montant</BTh>
            <BTh>Date</BTh>
          </BTr>
        </BThead>
        <BTbody>
          <BTr v-for="operation in operations" :key="operation.id">
            <BTd>{{ operation.id }}</BTd>
            <BTd>{{ operation.order_amount }}</BTd>
            <BTd>{{ operation.date }}</BTd>
          </BTr>
        </BTbody>
      </BTableSimple>
      <p v-else>Aucune opération trouvée.</p>
    </BTab>
    <BTab title="Very, very long title"><p>I'm the tab with the very, very long title</p></BTab>
    <BTab title="Disabled" disabled><p>I'm a disabled tab!</p></BTab>
  </BTabs>

</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ConfigSettings',
  components: {},
  props: {},
  data() {
    return {
      users: {
        id: 0,
        name: '',
        has_tr: false,
        tr_value: 0,
        tr_employee_share: 0,
        tr_employer_share: 0
      },
      operations: {
        id: 0,
        order_amount: 0,
        date: 0
      }
    }
  },
  mounted() {
    this.getUsers()
    this.getOperations()
  },
  methods: {
    getUsers() {
      console.log('getUsers')
      axios.get(this.$env.API_URL + 'users')
        .then(response => {
          console.log(response.data)
          this.users = response.data
        })
        .catch(error => {
          console.log(error)
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
          console.log(err)
        })
    }
  },
}
</script>

<style>

</style>
