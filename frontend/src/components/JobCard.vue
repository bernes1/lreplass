<script setup>
import { ref } from 'vue'
let companyName = ref("Intility AS")
let possiton = ref("IT-drift")
let location = ref("OSLO")
let applicationDeadline = ref("20.01.2023")
let datePosted = ref("10.01.2023")
let number_of_positions = ref("2 ")





</script>
<template>
  <div class="card w-85 bg-base-300 shadow-xl mt-5 mb-5 mx-5">
  <div class="card-body">
    <h2 class="card-title">{{ companyName }}</h2>
    <p>Fag: {{ possiton }}</p>
    <p>Lokasjon: {{ location }}</p>
    <p>Søknads frist: {{ applicationDeadline }}</p>
    <p>Dato lagt ut: {{datePosted}}</p>
    <p>Antal Stillinger: 2</p>
    <div class="card-actions justify-center">
      <button class="btn btn-primary"><a href="http://"></a>Link til stillingsannonse</button>
    </div>
  </div>
</div>
</template>