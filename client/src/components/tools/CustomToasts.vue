<template>
  <BToast v-model="active" variant="info">
    <template #title>
      Notification
    </template>
      Body
  </BToast>
</template>

<script>
export default {
  components: {

  },
  props: {
    active: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style>

</style>
