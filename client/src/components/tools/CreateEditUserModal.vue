<template>
  <div>
    <b-modal :visible="modelValue" title="Créer un utilisateur" @close="emitClose">
      <form>
        <div class="mb-3">
          <label for="name" class="form-label">Nom</label>
          <input type="text" class="form-control" id="name" v-model="user.name">
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" v-model="user.email">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Mot de passe</label>
          <input type="password" class="form-control" id="password" v-model="user.password">
        </div>
      </form>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'CreateEditUserModal',
  components: {},
  props: {
    dataForm: {
      type: Object,
      default: () => {}
    },
    modelValue: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      user: {}
    }
  },
  mounted() {

  },
  methods: {
    emitClose() {
      this.$emit('update:modelValue', false); // Fermer le modal
    },
  }
}
</script>

<style scoped>

</style>
