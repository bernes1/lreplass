<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">Læreplass</a>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal px-1">
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/drift">IT-Drift</RouterLink></li>
        <li><RouterLink to="/utvikling">IT-Utvikling</RouterLink></li>
      </ul>
    </div>
  </div>
</template>
