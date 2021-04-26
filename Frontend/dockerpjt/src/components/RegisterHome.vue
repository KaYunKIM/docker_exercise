<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="100"
        />
      </v-col>

      <v-col class="mb-4">
        <h4 class="display-2 font-weight-bold mb-3">
          Visitor Registration
        </h4>
        <!-- <p class="subheading font-weight-regular">
          <br>please type your name in
        </p> -->
      </v-col>
    </v-row>

  <v-form>
    <v-container>
      <v-row justify="center">
        <v-col md="3">
          <v-text-field
            solo
            label="Your Name Here"
            clearable
            v-model="visitor.visitor_name"
            @keypress.enter="addVisitor(visitor)"
          ></v-text-field>
        </v-col>
        
      </v-row>
    </v-container>
  </v-form>

  <v-row justify="center">
    <v-simple-table style="width:60%">
      <thead >
        <tr>
          <th class="text-center">
            Name
          </th>
          <th class="text-center">
            Time Stamp
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="visitor in visitorList"
          :key="visitor.visitor_name"
          class="text-center"
        >
          <td>{{ visitor.visitor_name }}</td>
          <td>{{ visitor.visit_datetime.slice(0,10)+' '+visitor.visit_datetime.slice(11,19) }}</td>
        </tr>
      </tbody>
    </v-simple-table>
  </v-row>

  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

  export default {
    name: 'RegisterHome',

    data: () => ({
      visitor: {
        "visitor_name": ''
      },
    }),
    
    computed: {
      ...mapState(['visitorList']),
    },

    methods: {
      ...mapActions(['fetchVisitorList', 'addVisitor']),
    },

    created() {
      this.fetchVisitorList()
    }
  }
</script>
