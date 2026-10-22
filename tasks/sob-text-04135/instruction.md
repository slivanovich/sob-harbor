Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Ernst Schlange: Ernst Schlange (September 1, 1888 – † 1947) was a Nazi German politician, Gauleiter of Berlin-Brandenburg and a member of the Prussian Landtag.  Severely wounded in World War I, he became active in various anti-Semitic far right political groups and eventually joined the National Socialist German Worker's Party in 1925.  He was opposed to the party's more extreme tactics for gaining power and eventually ran afoul of Reich Minister of Propaganda and Gauleiter of Berlin, Joseph Goebbels.  This caused Schlange to lose his leadership posts by the mid-1930s.  He died under obscure circumstances at the end of World War II.

Catholic bishops in Nazi Germany: Catholic bishops in Nazi Germany differed in their responses to the rise of Nazi Germany, World War II, and the Holocaust during the years 1933–1945.  In the 1930s, the Episcopate of the Catholic Church of Germany comprised 6 Archbishops and 19 bishops while German Catholics comprised around one third of the population of Germany served by 20,000 priests.  In the lead up to the 1933 Nazi takeover, German Catholic leaders were outspoken in their criticism of Nazism.  Following the Nazi takeover, the Catholic Church sought an accord with the Government, was pressured to conform, and faced persecution.  The regime had flagrant disregard for the Reich concordat with the Holy See, and the episcopate had various disagreements with the Nazi government, but it never declared an official sanction of the various attempts to overthrow the Hitler regime.  Ian Kershaw wrote that the churches "engaged in a bitter war of attrition with the regime, receiving the demonstrative backing of millions of churchgoers.  Applause for Church leaders whenever they appeared in public, swollen attendances at events such as Corpus Christi Day processions, and packed church services were outward signs of the struggle of ... especially of the Catholic Church - against Nazi oppression".  While the Church ultimately failed to protect its youth organisations and schools, it did have some successes in mobilizing public opinion to alter government policies.

Nazi control of the music medium: The nineteenth century introduced a change in economic circumstances in Germany.  The rise of industrialization and urban expansion introduced a new marketplace for music.  Individuals were able to participate within the music culture as small social clubs and orchestras were easily able to purchase sheet music and instruments.  Out of this developed an extensive network of music among German citizens.  The spawned more localized concert halls and orchestras, greatly increasing the circulation of both German and Jewish compositions.  Yet as the music culture grew the Nazi regime found it necessary to step in and control these cultural music products.  Joseph Goebbels, the Reich Minister of Propaganda, famously decreed the radio to be "the most influential and important intermediary between a spiritual movement and the nation, between the idea and the people".  He put much effort into the proliferation of radio technologies amongst German citizens regardless of socioeconomic status, introducing a low-cost people's receiver.  As the music industry of Nazi Germany grew, institutions within the regime devoted their efforts to promote Aryan ideologies through heavy censorship and cultural control.  From blacklisted Jewish compositions to banned concert hall performances Nazi intervention was obvious.  The regime issued strict authoritative control of these mediums in order to promote nationalism through cultural unity.

Mass suicides in 1945 Nazi Germany: During the final weeks of the Third Reich and the war in Europe, many civilians, government officials and military personnel throughout Nazi Germany committed suicide.  Aside from high-ranking Nazi officials like Adolf Hitler, Joseph Goebbels, Heinrich Himmler, Philipp Bouhler and Martin Bormann, many others chose " Selbstmord" (German: "Self-murder" ) rather than accept the defeat of Germany.  Studies have shown that the suicides were influenced through Nazi propaganda (reaction to the suicide of Adolf Hitler), the tenets of the Nazi Party, and the anticipated reprisals following the Allied occupation of Nazi Germany.  For example in April 1945, at least 1,000 people killed themselves and others within 72 hours as the Red Army neared the East German town of Demmin.

Rotraut Richter: Rotraut Richter (15 May 1915 – 1 October 1947) was a German stage and film actress.  She appeared in the role of Gerda in the 1933 Nazi propaganda film "Hitlerjunge Quex", receiving a letter of thanks from Joseph Goebbels along with the rest of the cast.

Joseph Goebbels: Paul Joseph Goebbels (] ; 29 October 1897 – 1 May 1945) was a German politician and Reich Minister of Propaganda of Nazi Germany from 1933 to 1945.  He was one of Adolf Hitler's close associates and most devoted followers, and was known for his skills in public speaking and his deep, virulent antisemitism, which was evident in his publicly voiced views.  He advocated progressively harsher discrimination, including the extermination of the Jews in the Holocaust.

Goebbels Diaries: The Goebbels Diaries are a collection of writings by Joseph Goebbels, a leading member of the German Nazi Party (NSDAP) and the Reich Minister of Public Enlightenment and Propaganda in Adolf Hitler's government from 1933 to 1945.  The diaries, which have only recently been published in full in German and are available only in part in English, are a major source for the inner history of the Nazi Party and of its twelve years in power in Germany.  The British historian Ian Kershaw wrote in the preface to his biography of Hitler: "For all the caution which must naturally be attached to Goebbels's regularly reported remarks by Hitler ... the immediacy as well as the frequency of the comments makes them a vitally important source of insight into Hitler's thinking and action. "

Fourth Reich: The Fourth Reich (German: "Viertes Reich" ) is a hypothetical future German empire that is the successor to Nazi Germany (1933–1945).  The term Third Reich was coined by Arthur Moeller van den Bruck as the title of his 1923 book "Das Dritte Reich".  It was used by the Nazis for propaganda purposes to legitimize their regime as a successor state to the retroactively-renamed First Reich (the Holy Roman Empire, 962–1806) and the Second Reich (Imperial Germany, 1871–1918).  The terms "First Reich" and "Second Reich" were never used by historians.

Reich Chamber of Culture: The Reich Chamber of Culture (Reichskulturkammer) was a government agency in Nazi Germany.  It was established by law on 22 September 1933 in the course of the "Gleichschaltung" process at the instigation of Reich Minister Joseph Goebbels as a professional organization of all German creative artists.  Defying the competing ambitions of the German Labour Front (DAF) under Goebbels' rival Robert Ley, it was meant to gain control over the entire cultural life in Germany creating and promoting Aryan art consistent with Nazi ideals.

Nazi Germany: Nazi Germany is the common English name for the period in German history from 1933 to 1945, when Germany was governed by a dictatorship under the control of Adolf Hitler and the Nazi Party (NSDAP).  Under Hitler's rule, Germany was transformed into a totalitarian state in which the Nazi Party controlled nearly all aspects of life.  The official name of the state was "Deutsches Reich" from 1933 to 1943 and "Großdeutsches Reich" ("Greater German Reich") from 1943 to 1945.  The period is also known under the names the Third Reich (German: "Drittes Reich" ) and the National Socialist Period (German: "Zeit des Nationalsozialismus" , abbreviated as "NS-Zeit").  The Nazi regime came to an end after the Allied Powers defeated Germany in May 1945, ending World War II in Europe.

Question: What was the role of a German stage and film actress who received a letter of thanks from a German politician and Reich Minister of Propaganda of Nazi Germany from 1933 to 1945?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the German stage and film actress."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the individual."
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    },
    "politician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the German politician and Reich Minister of Propaganda."
        },
        "title": {
          "type": "string",
          "description": "The title or role of the politician."
        }
      },
      "required": [
        "name",
        "title"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film in which the actress appeared."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "type": {
          "type": "string",
          "description": "The type or genre of the film."
        }
      },
      "required": [
        "title",
        "year",
        "type"
      ],
      "additionalProperties": false
    },
    "role_played": {
      "type": "string",
      "description": "The specific role played by the actress in the film."
    }
  },
  "required": [
    "actress_details",
    "politician_details",
    "film_details",
    "role_played"
  ],
  "additionalProperties": false
}
