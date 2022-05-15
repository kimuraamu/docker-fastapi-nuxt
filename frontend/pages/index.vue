<template>
  <div>
    名前は：{{ res.name }}です
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  async asyncData ({ app }) {
    const res = await app.$axios.$get('http://127.0.0.1/api/test_users/1')
    console.log(res)
    return { res }
  }
})
</script>