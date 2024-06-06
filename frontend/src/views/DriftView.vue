<template>
  <div class="h-screen">
    <div class="justify-center text-center">
      <h1 class="font-bold text-2xl">IT-Drift</h1>
    </div>
    <div class="justify-center grid grid-flow-row-dense grid-cols-auto grid-rows-auto md:grid-cols-3 md:grid-rows-3 mb-10 mt-15">
      <JobCard
        v-for="job in jobList"
        :key="job.id"
        :jobId="job.id"
        :companyName="job.company_name"
        :position="job.position"
        :location="job.location"
        :applicationDeadline="job.application_deadline"
        :datePosted="job.date_posted"
        :numberOfPositions="job.number_of_positions"
        :JobAdLink="job.job_ad_link"
      />
    </div>
    <Footer />
  </div>
</template>

<script>
import JobCard from '../components/JobCard.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    JobCard,
    Footer
  },
  data() {
    return {
      jobList: [] // Initialize as an empty array
    };
  },
  created() {
    this.fetchJobs();
  },
  methods: {
    async fetchJobs() {
      try {
        const response = await fetch('http://localhost:3000/api/v1/drift');
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.json();
        
        this.jobList = data;
        console.log('Updated jobList:', this.jobList);
         
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
    }
  }
};
</script>
