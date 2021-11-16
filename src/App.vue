<template>
  <v-app>
    <v-main>
      <v-container fill-height fluid class="primary">
        <v-row justify="center">
          <v-col cols="10" md="8" lg="6">
            <v-card class="rounded-lg" elevation="10">
              <v-card-title>Laruin ang mga salita</v-card-title>
              <v-card-subtitle
                >Ilagay sa input ang teksto at i-click ang Generate para laruin
                ang mga salita.</v-card-subtitle
              >
              <v-card-text>
                <v-textarea
                  v-model="input_text"
                  @input="handleInput"
                  label="Input"
                  autofocus
                  outlined
                  row-height="15"
                ></v-textarea>
                <v-textarea
                  v-model="output_text"
                  label="Resulta"
                  outlined
                  filled
                  row-height="15"
                  hide-details
                ></v-textarea>
              </v-card-text>
              <v-divider />
              <v-card-actions>
                <v-btn @click="clear">Clear</v-btn>
                <v-spacer />
                <v-btn @click="generate" color="primary">Generate</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
const syllableRegex =
  /[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?/gi;

function syllabify(word) {
  const ret = word.match(syllableRegex);
  if (ret == null) return [];
  return ret;
}

function reverse(s) {
  var o = "";
  for (var i = s.length - 1; i >= 0; i--) o += s[i];
  return o;
}

function syllableReverse(word) {
  const syllables = syllabify(word);
  if (syllables.length <= 1) return word;
  const last = syllables.pop();
  syllables.unshift(last);
  const ret = syllables.join("");
  if (Math.random() < 0.5) ret + "s";
  return ret;
}

function replaceFunction(from, to) {
  return function replaceAll(str) {
    return str.replace(new RegExp(from, "g"), to);
  };
}

export default {
  name: "App",

  components: {},

  data: () => ({
    input_text: "idol pagod si ako malupet dead power attacked cancelled gigil",
    output_text: "",
  }),

  methods: {
    clear() {
      this.input_text = "";
      this.output_text = "";
    },
    generate() {
      const words = this.input_text.toLowerCase().split(/[\s]+/);
      words.forEach((word, i) => {
        if (Math.random() < 0.6) return;

        let functions = [syllableReverse];
        if (Math.random < 0.5) functions.push(reverse);
        
        const last_char = word.substr(word.length - 1).toLowerCase();
        if (last_char === "a") functions.push((word) => word + "h");
        if (last_char === "o") functions.push((word) => word + "e");
        if (last_char === "d") functions.push((word) => word + "t");
        if (/g./.test(word.toLowerCase()))
          functions.push(replaceFunction("g", "q"));
        if (syllabify(word).includes("si"))
          functions.push(replaceFunction("si", "c"));
        if (word.toLowerCase().includes("k"))
          functions.push(replaceFunction("k", "c"));

        const func = functions[Math.floor(Math.random() * functions.length)];
        words[i] = func(word);
      });
      this.output_text = words.join(" ");
    },
    handleInput() {
      this.$nextTick(function () {
        this.input_text = this.input_text.replace(/[^A-Za-z\s]/g, "");
      });
    },
  },
};
</script>
