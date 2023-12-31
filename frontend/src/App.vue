<script setup>
import NavBar from './components/NavBar.vue'
import JobCard from './components/JobCard.vue';
</script>

<template>
  <header>
    <NavBar></NavBar>
  </header>
  <main class="md:container md:mx-auto">
    <div class="flex justify-center flex-col md:flex-row mb-10 mt-10" >
        <JobCard></JobCard>
        <JobCard></JobCard>
        <JobCard></JobCard>
    </div>
  </main>
  <footer class="footer footer-center p-4 bg-base-300 text-base-content">
  <aside>
    <p>Copyright © 2023 - All rights reserved</p>
  </aside>
</footer>
</template>