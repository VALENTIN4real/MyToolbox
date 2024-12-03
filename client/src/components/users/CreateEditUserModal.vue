<template>
  <div>
    <b-modal :visible="modelValue" title="Créer un utilisateur" @ok="handleOk" @show="open" @hidden="emitClose">
      <form>
        <div class="mb-3">
          <label for="name" class="form-label">Nom</label>
          <input type="text" class="form-control" id="name" v-model="user.name">
        </div>
        <div class="mb-3">
          <h4>Titres-restaurant</h4>
        </div>
        <BInputGroup class="mb-2" append="€">
          <BInputGroupText>
            <BFormCheckbox class="me-n2" v-model="user.has_tr">
              <span class="">TR</span>
            </BFormCheckbox>
          </BInputGroupText>
          <BFormInput type="number" placeholder="Montant TR" v-model="user.tr_value" :disabled="!user.has_tr"/>
        </BInputGroup>
        <BInputGroup class="mb-2" append="€">
          <BFormInput type="number" placeholder="Part salariale" v-model="user.tr_employee_share" :disabled="!user.has_tr"/>
        </BInputGroup>
        <BInputGroup class="mb-2" append="€">
          <BFormInput type="number" placeholder="Part patronale" v-model="user.tr_employer_share" :disabled="!user.has_tr"/>
        </BInputGroup>
        <BButton v-if="user.id > 0" variant="danger" @click="deleteUser">Supprimer</BButton>
      </form>
    </b-modal>
  </div>
</template>

<script>

import { cloneDeep } from 'lodash'
import axios from 'axios'

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
      user: []
    }
  },
  watch: {
    dataForm: {
      deep: true,
      immediate: true,
      handler(newDataForm) {
        this.user = cloneDeep(newDataForm)
      }
    },
    user: {
      deep: true,
      handler() {
        this.calculThirdValue()
      }
    }

  },

  methods: {
    open() {
      console.log(this.user)
      console.log(this.dataForm)
    },
    emitClose() {
      console.log("emitClose")
      console.log(this.user)
      console.log(this.dataForm)
      this.$emit('update:modelValue', false)
    },
    calculThirdValue() {
      console.log("calculThirdValue triggered");

      if (this.user.has_tr) {
        if (this.user.tr_value > 0 && this.user.tr_employee_share > 0) {
          const newEmployerShare = this.user.tr_value - this.user.tr_employee_share;
          if (this.user.tr_employer_share !== newEmployerShare) {
            this.user.tr_employer_share = newEmployerShare;
          }
        } else if (this.user.tr_value > 0 && this.user.tr_employer_share > 0) {
          const newEmployeeShare = this.user.tr_value - this.user.tr_employer_share;
          if (this.user.tr_employee_share !== newEmployeeShare) {
            this.user.tr_employee_share = newEmployeeShare;
          }
        } else if (this.user.tr_employee_share > 0 && this.user.tr_employer_share > 0) {
          const newTrValue = this.user.tr_employee_share + this.user.tr_employer_share;
          if (this.user.tr_value !== newTrValue) {
            this.user.tr_value = newTrValue;
          }
        }
      }
    },
    handleOk() {
      if (this.user.id) {
        this.updateUser()
      } else {
        this.createUser()
      }
    },
    createUser() {
      axios.post(this.$env.API_URL + 'users', this.user)
        .then(response => {
          console.log(response.data)
          this.$emit('refreshUsers')
        })
        .catch(err => {
          console.error(err)
        })
    },
    updateUser() {
      axios.put(this.$env.API_URL + 'users/' + this.user.id, this.user)
        .then(response => {
          console.log(response.data)
          this.$emit('refreshUsers')
        })
        .catch(error => {
          console.error(error)
        })
    },
    deleteUser() {
      axios.delete(this.$env.API_URL + 'users/' + this.user.id)
        .then( res => {
          console.log(res.data)
          this.$emit('refreshUsers')
          this.emitClose()
        })
        .catch(err => {
          console.error(err)
        })
    }
  }
}
</script>

<style scoped>

</style>
