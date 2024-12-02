<template>
  <div>
    <b-modal :visible="modelValue" title="Créer un utilisateur" @show="open" @hidden="emitClose">
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
      </form>
    </b-modal>
  </div>
</template>

<script>

import { cloneDeep } from 'lodash'

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
  }
}
</script>

<style scoped>

</style>
