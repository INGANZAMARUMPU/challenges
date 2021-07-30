ce fichie .vue permet d'afficher les bulles de nofication pendant 5 sec 

pour le rendre fonctionnel tu dois le mettre dans le dossier
des components et definir une variable dans le store.

```js 
notification:{type:"", message:""}
```

les types sont:
	- danger
	- success

une type vide utilise par defaut la couleur #48d

le component va ètre appelé dans le fichier App.vue comme suit
par exemple :

```js
<template>
  <div class="body">
    <div v-if="is_logged_in" class="maincontent">
      <Menus/>
      <router-view/>
      <Footer/>
      <Notifier/>
    </div>
    <LoginForm v-else/>
  </div>
</template>
<script>
//...
import Notifier from "./components/notifier"
//...

export default {
  //...
  components: {
    LoginForm, Menus, Footer, Notifier
  },
  //...
};
</script>
<style src="./style.css">
</style>
```

pour afficher la notiffication alors à partir de n'importe quel component 
vous aurez seulement à faire:

```js
  this.$store.state.notification = {
    type:"danger",
    message:"l'intervalle que vous avez donné est invalide."
  }
```