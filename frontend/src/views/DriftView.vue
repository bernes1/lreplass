<script>
import JobCard from '../components/JobCard.vue'
import jobListings from '../assets/jobListings.json'
import Footer from '@/components/Footer.vue';
export default {
  components: {
    JobCard,
    Footer
  },
  data() {
    return {
      jobList: jobListings
    };
  },
};
</script>


<template>
  <div class="h-screen">
    <div class="justify-center text-center">
      <h1 class="font-bold text-2xl">IT-Drift</h1>
    </div>

  <div class="justify-center grid grid-flow-row-dense grid-cols-auto grid-rows-auto  md:grid-cols-3 md:grid-rows-3  mb-10 mt-15">
    <JobCard
      v-for="job in jobList"
      :key="job.jobId"
      :jobId="job.jobId"
      :companyName="job.companyName"
      :position="job.position"
      :location="job.location"
      :applicationDeadline="job.applicationDeadline"
      :datePosted="job.datePosted"
      :numberOfPositions="job.numberOfPositions"
      :JobAdLink="job.JobAdLink"
    />
  </div>  
<Footer></Footer>
  </div>
</template>
