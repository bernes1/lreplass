<template>
  <div class="card w-85 bg-base-300 shadow-xl mt-5 mb-5 mx-5">
  <div class="card-body">
    <h2 class="card-title">{{ companyName }}</h2>
    <p>Fag: {{ position }}</p>
    <p>Lokasjon: {{ location }}</p>
    <p>Søknads frist: {{ applicationDeadline }}</p>
    <p>Dato lagt ut: {{ datePosted }}</p>
    <p>Antal Stillinger: {{ numberOfPositions }}</p>
    <div class="card-actions justify-center">
      <button class="btn btn-primary"><a :href="JobAdLink">Link til stillingsannonse</a></button>
    </div>
  </div>
</div>
</template>

<script>

export default {
  props: {
    jobId: Number,
    companyName: String,
    position: String,
    location: String,
    applicationDeadline: String,
    datePosted: String,
    numberOfPositions: Number,
    JobAdLink: String
  },
};


</script>