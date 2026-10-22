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
Eduard Schulte: Eduard Schulte ( 4 January 1891 in Düsseldorf – 6 January 1966 in Zürich) was a prominent German industrialist.  He was one of the first to warn the Allies and tell the world of the Holocaust and systematic exterminations of Jews in Nazi Germany occupied Europe.

Holocaust theology: Holocaust theology is a body of theological and philosophical debate concerning the role of God in the universe in light of the Holocaust of the late 1930s and 1940s.  It is primarily found in Judaism; Jews were drastically affected by the Holocaust, in which six million Jews were murdered in a genocide by Nazi Germany and its allies.  Jews were killed in higher proportions than other groups; some scholars limit the definition of the Holocaust to the Jewish victims of the Nazis as Jews alone were targeted for the Final Solution.  Others include the additional five million non-Jewish victims, bringing the total to about 11 million.  One third of the total worldwide Jewish population were killed during the Holocaust.  The Eastern European Jewish population was particularly hard hit, being reduced by ninety percent.  While a disproportionate number of Jewish religious scholars were killed, more than eighty percent of the world’s total, the perpetrators of the Holocaust did not merely target religious Jews.  A large percentage of the Jews killed both in Eastern and Western Europe were either nonobservant or had not received even an elementary level Jewish education.

Oskar Schindler: Oskar Schindler (28 April 1908 – 9 October 1974) was a German industrialist, spy, and member of the Nazi Party who is credited with saving the lives of 1,200 Jews during the Holocaust by employing them in his enamelware and ammunitions factories, which were located in occupied Poland and the Protectorate of Bohemia and Moravia.  He is the subject of the 1982 novel "Schindler's Ark" and its 1993 film adaptation, "Schindler's List", which reflected his life as an opportunist initially motivated by profit, who came to show extraordinary initiative, tenacity, and dedication to save the lives of his Jewish employees.

Jacob Muschong: Jacob Muschong or Iacob Muschong (born 1868, Nagykikinda, Austria-Hungary - died December 13, 1923, Lugoj, Romania) was an ethnic German industrialist who made a fortune producing bricks.  He was born in Nagykikinda (Serbian: "Velika Kikinda, "now "Kikinda", Serbia), a town in the Banat, in a family with a long tradition in the production of bricks.  His grandparents and great-grandparents han produced bricks in workshops located at the edge of Lugoj.  At the age of 20 years he married Margaret Bohn the daughter of a famous German industrialist specialized in the production of tiles and bricks that built the brick factory at Zsombolya (now Jimbolia, Romania) and Gyertyámos (Cărpiniş) and had other several factories in Europe.

Clerical People's Party: Kyrkliga Folkpartiet (English: Clerical People's Party or Popular Party) a minor pro-fascist party in Sweden founded in 1930.  The party was formed a led by Ivar Rhedin, a priest in the Church of Sweden.  Rhedin was the editor of "Göteborgs Stiftstidning" ("Magazine of the Diocese of Gothenburg"), in which he wrote many pro-German articles.  The party was an ally of the main Nazi party in Sweden, National Socialist Workers Party.  But the cooperation between the two parties didn't last.  Although both groups were staunch antisemites, their approaches toward the Jews were somewhat different.  Rhedin, as a conservative Christian, was against the Jews as a religious community.  NSAP were against the Jews as a race.  Rhedin had no problem in accepting Jews who converted to Christianity, whereas NSAP and other nazi groups considered that converted Jews continued to be Jews in racial aspects.  The party was closed down in 1936.

Marcinkonys Ghetto: Marcinkonys or Marcinkance Ghetto was a Jewish ghetto established in Marcinkonys, Lithuania, during the Holocaust.  The ghetto was set up at the end of 1941 and covered the area of 1.5 ha , surrounded by barbed wire.  Several hundred people lived in the improvised ghetto.  On November 2, 1942, orders were given to liquidate the ghetto and transport the Jews to Treblinka and Auschwitz concentration camps.  A squad of 15 Germans ordered the Jews to gather at the entrance at 8am to be "transported for labor."  Witnesses present different accounts of further events.  According to an official complaint written by forester Hans Lehmann, two of the Germans opened fire at the crowded Jews without a reasonable cause.  Other authors present the events as a revolt inspired by Aaron Kobrowski, chairman of the Judenrat.  Panicked Jews attempted to escape through the fence into the nearby forest or back into the ghetto.  The Germans then searched the ghetto, shooting any Jews on sight and destroying five secret bunkers.  In total, 105 or 132 Jews were shot.  About a hundred Jews escaped and 45 of them survived the war.  Hans Lehmann, who had joined the Nazi Party in 1933, was investigated and it was determined that he was sympathetic to the Jews and allowed them to escape.  He was discredited and transferred.  In 1943, Jewish partisans derailed a German train east of Białystok.  Lehmann was among the captured Germans.  He recognized by one of the escapees from Marcinkonys and executed for his role in the massacre.

Berthold Beitz: Berthold Beitz (26 September 1913 – 30 July 2013) was a German industrialist.  He was the head of the Krupp steel conglomerate beginning in the 1950s.  He was credited with helping to lead the re-industrialization of the Ruhr Valley and rebuilding Germany into an industrial power.  He gained acclaim for saving some 250 Jewish workers during World War II by declaring them to be essential workers at an oil facility in Poland.  In 1973, for saving Jews, he received the Righteous Among the Nations title awarded by the Israeli Yad Vashem, the highest honor given to a non-Jew.

Abraham Bankier: Abraham Bankier (1910-1956) was one of the owners of the "Rekord" factory on Lipowa street in Cracow, Poland, that Oskar Schindler took over during World War II.  Schindler then hired Bankier to manage the factory, which was renamed "Deutsche Emailwarenfabrik Oskar Schindler", "Emalia" for short.  Bankier was able to leverage black market dealings with extra scrap metal to bring additional Jews to work at the factory, thereby giving them a reprieve and ultimately saving many lives.

Berlin-Lübecker Maschinenfabrik: Berlin-Lübecker Maschinenfabrik (BLM) was a manufacturer of handguns, infantry rifles, ammunition up to 2 cm, flareguns and precision military equipment in Germany from 1936 to 1945.  The company, based in Lübeck, Germany, was one of a number of metal-related businesses owned by Bernhard Berghaus, a German industrialist and member of the Nazi party who played an important role in the rearmament of Germany during the Third Reich.

Adversus Judaeos: Adversus Judaeos (Greek "Kata Ioudaiōn", "against the Jews" or "against the Judeans") are a series of fourth century homilies by John Chrysostom directed to members of the church of Antioch of his time, who continued to observe Jewish feasts and fasts.  Critical of this, he cast Judaism and the synagogues in his city in a critical and negative light.  There are modern scholars who claim that an abuse of his preaching fed later Christian anti-Semitism, and some, such as Stephen Katz, go even further, saying it was an inspiration for pagan Nazi anti-semitism with its evil fruit of the programme to annihilate the Jewish race.  Indeed, during World War II, the Nazi Party in Germany abused his homilies, quoting and reprinting them frequently in an attempt to legitimize the Holocaust in the eyes of German and Austrian Christians.  Christian priest James Parkes called the writing on Jews "the most horrible and violent denunciations of Judaism to be found in the writings of a Christian theologian".  His sermons against Jews gave further momentum to the idea that Jews are collectively responsible for the death of Jesus.

Question: Abraham Bankier was one of the owners of the Rekord factory that was taken over by a German Industrialist, spy, and member of the Nazi Party who is credited with saving how many Jews during the Holocaust?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rescuer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the industrialist who saved Jews."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the industrialist."
        },
        "roles_and_affiliations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles and affiliations of the industrialist."
        }
      },
      "required": [
        "name",
        "nationality",
        "roles_and_affiliations"
      ],
      "additionalProperties": false
    },
    "factory_details": {
      "type": "object",
      "properties": {
        "original_name": {
          "type": "string",
          "description": "The original name of the factory taken over."
        },
        "original_owner_name": {
          "type": "string",
          "description": "The name of one of the original owners of the factory."
        }
      },
      "required": [
        "original_name",
        "original_owner_name"
      ],
      "additionalProperties": false
    },
    "jews_saved_count": {
      "type": "integer",
      "description": "The number of Jews credited with being saved by the industrialist."
    },
    "historical_event": {
      "type": "string",
      "description": "The historical event during which the saving occurred."
    }
  },
  "required": [
    "rescuer_details",
    "factory_details",
    "jews_saved_count",
    "historical_event"
  ],
  "additionalProperties": false
}
