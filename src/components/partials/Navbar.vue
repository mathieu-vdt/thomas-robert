<script lang="ts">
import { ref, computed, watch } from 'vue'
import { pictures } from '../../utilities/pictures'

let menuOpen = ref(false)
let isMobile = computed(() => window.innerWidth <= 768)

watch(isMobile, (newValue) => {
  if (!newValue) {
    menuOpen.value = true
  }
})

export default {
  data() {
    return {
      pictures,
      menuOpen: false // Add this line
    }
  }
}
</script>

<template>
  <nav>
    <a href="thomas-robert/"><div class="logo">Portfolio</div></a>
    <ul :class="{ 'slide-in': menuOpen }">
      <a href="#home"><li>À propos</li></a>
      <a href="#about-me"><li>Outils maitrisés</li></a>
      <a href="#experience"><li>Expériences</li></a>
      <!-- <div class="socials-mobile">
        <a href="#"><font-awesome-icon :icon="['fab', 'linkedin-in']" /></a>
        <a href="#"><font-awesome-icon :icon="['fab', 'github']" /></a>
      </div> -->
    </ul>
    <!-- <div class="socials">
      <a href="#"><font-awesome-icon :icon="['fab', 'linkedin-in']" /></a>
      <a href="#"><font-awesome-icon :icon="['fab', 'github']" /></a>
    </div> -->
    <a href="#" class="menu-burger" @click.prevent="menuOpen = !menuOpen">
      <font-awesome-icon v-if="!menuOpen" :icon="['fas', 'bars']" />
      <font-awesome-icon v-else :icon="['fas', 'xmark']" />
    </a>
  </nav>
</template>
<style lang="scss">
nav {
  display: flex;
  background-color: transparent;
  padding: 20px 30px;
  flex-direction: row;
  color: var(--black);
  font-size: 1.5em;
  align-items: center;
  justify-content: space-between;

  a {
    text-decoration: none;
    color: var(--black);
  }
  ul {
    display: flex;
    flex-direction: row;
    list-style-type: none;
    margin: 0;
    padding: 0;
    transition: transform 0.3s ease;
    a {
      margin-right: 10px;
      text-decoration: none;
      color: var(--black);
      font-weight: 500;
      padding: 5px;
      transition: all 0.3s ease;

      &:hover {
        color: #ec723d;
      }
    }

    .socials-mobile {
      display: none;
    }
  }

  .logo {
    display: flex;
    align-items: center;
    flex-direction: row;
    column-gap: 10px;
    color: var(--black);
    font-size: 1.2em;
    font-weight: bold;

    img {
      width: 30px;
      height: 30px;
    }
  }

  .socials {
    a {
      color: var(--black);
      font-size: 1.2em;
      margin-left: 10px;
      transition: all 0.3s ease;

      &:hover {
        color: var(--dark-purple);
      }
    }
  }

  .menu-burger {
    display: none;
    text-decoration: none;
    color: var(--black);
  }
}

@media screen and (max-width: 768px) {
  nav {
    padding: 20px 20px;
    align-items: center;
    justify-content: space-between;

    ul {
      background-color: var(--white);
      flex-direction: column;
      text-align: center;
      width: 100vw;
      height: 100vh;
      top: 0;
      left: 0;
      padding-top: 50px;
      transform: translateX(-100vw);
      position: fixed;
      z-index: 1000;

      a {
        padding: 20px;
        margin: 0;
        width: 100%;

        &:hover {
          color: var(--white);
          background-color: #ec723d;
        }
      }

      .socials-mobile {
        display: block;
        a {
          padding: 20px;
          margin: 0;
          width: 100%;
          font-size: 1.3em;

          &:hover {
            color: var(--black);
            background-color: transparent;
          }
        }
      }
      &.slide-in {
        transform: translateX(0);
      }
    }

    .svg-inline--fa.fa-xmark {
      padding: 20px;
      position: fixed;
      top: 0;
      right: 0;
      z-index: 1000;
      font-size: 1.5em;
    }

    .socials {
      display: none;
    }

    .menu-burger {
      display: block;
      font-size: 1.5em;
    }
  }
}
</style>
