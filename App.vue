<template>
  <div id="app">
    <Nav/>
    <FlashMessage/>
    <router-view/>
  </div>
</template>
<script>
import Nav from "@/components/Nav.vue";
import Vue from 'vue';
import FlashMessage from '@smartweb/vue-flash-message';
Vue.use(FlashMessage);
export default {
  name: "Main",
  components: {
    Nav,
    FlashMessage
  }
};
</script>
<style>
body{
  background-image: url('https://bitdefender.pl/wp-content/uploads/2018/09/features-background-ultra.jpg');
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
