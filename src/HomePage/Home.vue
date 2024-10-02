<script lang="ts">
import { ref, computed, watch } from 'vue'
import { pictures } from '../utilities/pictures'

export default {
  data() {
    return {
      pictures
    }
  },
  computed: {
    waveStyle() {
      return {
        background: `url(${this.pictures.wave}) repeat-x`,
        backgroundSize: '200% 100%',
        animation: 'wave 20s infinite linear alternate-reverse'
      }
    }
  }
}
</script>

<template>
  <div id="home">
    <div class="job">
      <div class="position">
        <p class="full-stack">THOMAS</p>
        <p class="dev">ROBERT</p>
      </div>
      <a class="contact-me" href="https://linktr.ee/daaaalin" target="_blank">Contact me</a>
    </div>
    <div class="profile">
      <div class="showreel">
        <a href="https://youtu.be/oIW_e8Cob0E" target="_blank"><p>SHOWREEL</p></a>
        <iframe
          width="893"
          height="502"
          src="https://www.youtube.com/embed/oIW_e8Cob0E"
          title="Showreel THOMAS ROBERT"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
        ></iframe>
      </div>
      <br />
      <p class="im">Vidéaste & Monteur</p>
      <div class="presentation">
        <p class="desc">
          Je fais du montage depuis quatre ans, principalement sur After Effects . Je maîtrise le
          Compositing, le Motion Design et la VFX, tout en étant également compétent en 3D avec
          Blender. Je réalise des prises de vue vidéo avec un Sony FX3 et m'occupe de l'étalonnage
          sur DaVinci Resolve. Passionné et créatif, j'aime donner vie à des projets visuels
          percutants.
        </p>
      </div>
    </div>
    <div class="wave-top" :style="waveStyle"></div>
    <div class="wave-mid" :style="waveStyle"></div>
    <div class="wave-bottom" :style="waveStyle"></div>
  </div>
</template>

<style lang="scss">
#home {
  /* background: linear-gradient(178deg, rgba(255, 255, 255, 0.5) 0%, rgba(177, 177, 177, 0.5) 100%);*/
  position: relative;
  width: 100%;
  overflow: hidden;
  min-height: calc(100vh - 74px);
  overflow: hidden;
  display: flex;
  flex-direction: row;

  .job {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .position {
      p {
        font-size: 7rem;
        font-weight: 600;
        color: var(--black);
        line-height: 1.2em;

        &.dev {
          margin-left: 200px;
          background: linear-gradient(0deg, var(--black) 40%, var(--black) 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
      }
    }

    a.contact-me {
      text-decoration: none;
      font-size: 1.5rem;
      padding: 10px 40px;
      border: none;
      border-radius: 70px;
      background-color: #ec723d;
      color: var(--white);
      transition: all 0.3s;
    }

    a.contact-me:hover {
      cursor: pointer;
      background-color: #d26030;
      transition: all 0.3s;
    }
  }
  .profile {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    // align-items: center;
    color: var(--black);
    padding: 10px;

    img {
      background-color: #d9d9d9a2;
      height: 400px;
      border-radius: 80%;
    }

    p.im {
      font-size: 3rem;
      font-weight: 600;

      text-align: left;
      line-height: 1em;
    }

    p.desc {
      font-size: 1.5rem;
      margin-top: 20px;
      text-align: left;
      line-height: 1em;
      width: 100%;
    }
  }

  .wave-top,
  .wave-mid,
  .wave-bottom {
    position: absolute;
    z-index: -1;
    top: -10%;
    width: 100%;
    height: 100vh;
  }

  .wave-top {
    transform: rotate(-5deg);
  }
  .wave-bottom {
    transform: rotate(5deg);
  }

  .showreel {
    background-color: #ec723d;
    font-weight: bold;
    color: white;
    width: 100%;
    padding: 10px;
    transition: all 0.3s;
    a {
      text-decoration: none;
      font-weight: bold;
      color: white;

      p {
        font-size: 1.5rem;
        text-align: center;
        transition: all 0.3s;
      }
    }

    iframe {
      width: -webkit-fill-available;
      height: 0; /* Hauteur initiale à 0 pour masquer */
      opacity: 0; /* L'iframe est invisible au départ */
      transition:
        height 0.5s ease,
        opacity 0.5s ease; /* Transition sur la hauteur et l'opacité */
      overflow: hidden;
    }
  }

  .showreel:hover {
    cursor: pointer;
    background-color: #c85f32;
    transition: all 0.3s;
    p {
      transition: all 0.3s;
    }
    iframe {
      height: 300px; /* La hauteur nécessaire pour l'iframe */
      opacity: 1; /* L'iframe devient visible */
      transition:
        height 0.5s ease,
        opacity 0.5s ease;
    }
  }
}

@keyframes wave {
  0% {
    background-position: 0% 0;
  }
  100% {
    background-position: 100% 0;
  }
}

@media screen and (max-width: 1550px) {
  #home {
    .job {
      .position {
        p {
          font-size: 5rem;
        }
      }
      button.contact-me {
        font-size: 1rem;
        margin-right: 0px;
        margin-top: 20px;
      }
    }

    .profile {
      img {
        background-color: #d9d9d9a2;
        height: 300px;
        border-radius: 80%;
      }

      .presentation {
        p.im {
          font-size: 2.5rem;
          font-weight: 600;

          line-height: 1em;
        }

        p.desc {
          font-size: 1.5rem;
          width: 100%;
        }
      }
    }
  }
}

@media screen and (max-width: 1100px) {
  #home {
    position: initial;
    flex-direction: column;

    .job {
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-bottom: 10%;
      margin-top: 10%;

      .position {
        p {
          font-size: 5rem;
        }
      }
      button.contact-me {
        font-size: 1rem;
        margin-right: 0px;
        margin-top: 20px;
      }
    }

    .profile {
      justify-content: center;
      align-items: center;
      width: 100%;

      img {
        background-color: #d9d9d9a2;
        height: 300px;
        border-radius: 80%;
      }

      .presentation {
        padding: 0 20px;
        p.im {
          margin-top: 20px;
          font-size: 2rem;
          font-weight: 600;

          text-align: center;
          line-height: 1em;
        }

        p.desc {
          font-size: 1.5rem;
          text-align: center;
          width: 100%;
        }
      }
    }

    .wave-top,
    .wave-mid,
    .wave-bottom {
      position: fixed;
      top: -28%;
    }
  }
}

@media screen and (max-width: 768px) {
  #home {
    position: initial;
    flex-direction: column;

    .job {
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-bottom: 10%;
      margin-top: 10%;

      .position {
        p {
          font-size: 3rem;

          &.dev {
            margin-left: 60px;
          }
        }
      }
      button.contact-me {
        font-size: 1rem;
        margin-right: 0px;
        margin-top: 20px;
      }
    }

    .profile {
      width: 100%;

      img {
        background-color: #d9d9d9a2;
        height: 200px;
        border-radius: 80%;
      }

      .presentation {
        padding: 0 20px;
        p.im {
          margin-top: 20px;
          font-size: 2rem;
          font-weight: 600;

          text-align: center;
          line-height: 1em;
        }

        p.desc {
          font-size: 1.2rem;
          text-align: center;
          width: 100%;
        }
      }
    }

    .wave-top,
    .wave-mid,
    .wave-bottom {
      position: fixed;
      top: -28%;
    }
  }
}
</style>
