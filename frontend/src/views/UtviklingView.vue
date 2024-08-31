<script>
import Joblisting from '@/components/JobListing.vue'
</script>

<template>
  <Joblisting apiUrl="utvikling" pageName="IT-Utvikling" />

  export default {
    components: {
        Joblisting
    }
};
</template>