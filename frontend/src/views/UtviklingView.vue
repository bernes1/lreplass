<template>
  <div class="h-screen">
    <div class="justify-center text-center">
      <h1 class="font-bold text-2xl">IT-Utvikling</h1>
    </div>
    <div v-if="errorMessage" class="text-center text-red-500">
      <p>{{ errorMessage }}</p>
    </div>
    <div class="justify-center grid grid-flow-row-dense grid-cols-auto grid-rows-auto md:grid-cols-3 md:grid-rows-3 mb-10 mt-15">
      <JobCard
        v-for="job in jobList"
        :key="job.id"
        :jobId="job.id"
        :companyName="job.company_name"
        :position="job.position"
        :location="job.location"
        :applicationDeadline="formatDate(job.application_deadline)"
        :datePosted="formatDate(job.date_posted)"
        :numberOfPositions="job.number_of_positions"
        :JobAdLink="job.job_ad_link"
      />
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from 'axios';
import JobCard from '@/components/JobCard.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    JobCard,
    Footer
  },
  data() {
    return {
      jobList: [], // Initialize as an empty array
      errorMessage: '' // Initialize error message as an empty string
    };
  },
  created() {
    this.fetchJobs();
  },
  methods: {
    async fetchJobs() {
      try {
        const response = await axios.get('utvikling');
        this.jobList = response.data.data;
        this.errorMessage = ''; 
      } catch (error) {
        this.errorMessage = 'Det oppstod ett problem. Prøv igjen senere.';
        console.error('There was a problem with the fetch operation:', error);
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
      return date.toLocaleDateString('nb-NO', options);
    }
  }
};
</script>
