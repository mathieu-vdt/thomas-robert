<script lang="ts">
import TitleNumber from '../components/TitleNumber.vue'
import CardExperience from '../components/CardExperience.vue'
import Carousel from 'primevue/carousel'
import { pictures } from '@/utilities/pictures'
import Experience from './Experience.vue'

export default {
  components: {
    TitleNumber,
    CardExperience,
    Carousel
  },
  data() {
    return {
      experiences: [
        {
          title: 'Agent Polyvalent Audiovisuel et Numérique',
          status: '15 mois',
          date: '2023-2024',
          description:
            "Réaliser les tournages, enregistrements, et montages des séquences vidéo et photo, effectuer la post-production (montage, mixage, colorimétrie), l'habillage graphique et titrage, installer le matériel sur site avec réglage de l'éclairage et du son, et assurer l'assistance maintenance numérique."
        },
        {
          title: 'Stage (BTS Système Numérique)',
          status: '6 semaines',
          date: '2022',
          description:
            "Assurer la gestion de l'assistance aux utilisateurs, le dépannage des systèmes et réseaux, ainsi que la gestion de l'espace numérique communal."
        }
      ],
      responsiveOptions: [
        {
          breakpoint: '1400px',
          numVisible: 2,
          numScroll: 1
        },
        {
          breakpoint: '1199px',
          numVisible: 2,
          numScroll: 1
        },
        {
          breakpoint: '745px',
          numVisible: 1,
          numScroll: 1
        },
        {
          breakpoint: '575px',
          numVisible: 1,
          numScroll: 1
        }
      ],
      pictures
    }
  }
}
</script>

<template>
  <div id="about-me">
    <img :src="pictures.triangle" alt="triangle" class="triangle" />
    <img :src="pictures.triangle_o" alt="triangle" class="triangle_o" />
    <TitleNumber number="01" title="Outils maitrisés" />

    <div class="all-progress">
      <div class="progress">
        <img :src="pictures.ai" alt="" class="progress-img" />

        <div>
          <p>Adobe illustrator</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
      <div class="progress">
        <img :src="pictures.ps" alt="" class="progress-img" />
        <div>
          <p>Adobe Photoshop</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
      <div class="progress">
        <img :src="pictures.pr" alt="" class="progress-img" />
        <div>
          <p>Adobe Premiere Pro</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
      <div class="progress">
        <img :src="pictures.blender" alt="" class="progress-img" />
        <div>
          <p>Blender</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
      <div class="progress">
        <img :src="pictures.ae" alt="" class="progress-img" />
        <div>
          <p>Adobe After Effects</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
      <div class="progress">
        <img :src="pictures.davinci" alt="" class="progress-img" />
        <div>
          <p>DaVinci Resolve</p>
          <progress value="70" max="100">70 %</progress>
        </div>
      </div>
    </div>

    <br />
    <div id="experience">
      <TitleNumber number="02" title="Expériences professionnelles" />
      <p class="description">
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veritatis ea quas cumque,
        assumenda eligendi repudiandae magni i.
      </p>

      <Carousel
        :value="experiences"
        :numVisible="3"
        :numScroll="3"
        :responsiveOptions="responsiveOptions"
      >
        <template #item="slotProps">
          <CardExperience
            :title="slotProps.data.title"
            :status="slotProps.data.status"
            :date="slotProps.data.date"
            :description="slotProps.data.description"
            class="card-experience"
            style="height: 100%"
          />
        </template>
      </Carousel>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#about-me {
  background: linear-gradient(0, #e3e3e3 0%, #ffffffb9 100%);
  width: 100%;
  padding: 40px;
  color: var(--black);
  position: relative;
  z-index: 1;
  overflow: hidden;

  .all-progress {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    column-gap: 20px;
    row-gap: 20px;
    padding: 60px;
  }
  .progress {
    display: flex;
    flex-direction: row;
    align-items: center;

    progress {
      accent-color: #585247;
    }

    img {
      width: 50px;
      height: auto;
      margin-right: 10px;
    }
  }
  .triangle {
    position: absolute;
    z-index: -1;
    right: 0;
    top: 350px;
  }

  .triangle_o {
    position: absolute;
    z-index: -1;
    left: 10%;
    top: 0;
    transform: rotate(60deg);
    opacity: 0.6;
  }
  .description {
    font-size: 1.2em;
    font-weight: 400;
    width: 50%;
    margin-bottom: 20px;
  }
  .card-experience {
    margin: 0 20px; /* Adjust as needed */
  }
}

@media screen and (max-width: 900px) {
  #about-me {
    height: auto;
    width: 100%;
    .description {
      width: 80%;
    }

    .all-progress {
      padding: 0;
    }
  }
}

@media screen and (max-width: 600px) {
  #about-me {
    padding: 20px;
    .description {
      width: 100%;
    }
  }
}
</style>
