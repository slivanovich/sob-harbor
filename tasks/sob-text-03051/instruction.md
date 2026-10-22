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
Mihai Ralea: Mihai Dumitru Ralea (also known as Mihail Ralea, Michel Raléa, or Mihai Rale; May 1, 1896 – August 17, 1964) was a Romanian social scientist, cultural journalist, and political figure.  He debuted as an affiliate of Poporanism, the left-wing agrarian movement, which he infused with influences from corporatism and Marxism.  A distinguished product of French academia, Ralea rejected traditionalism and welcomed cultural modernization, outlining the program for a secular and democratic "peasant state".  His ideology blended into his scholarly work, with noted contributions to political sociology, the sociology of culture, and social and national psychology.  He was a professor at the University of Iași and, from 1938, the University of Bucharest.

Bulgarian Agrarian National Union: Bulgarian Agrarian National Union also translated to English as Bulgarian Agrarian People's Union (Bulgarian: Български земеделски народен съюз , "Bǎlgarski Zemedelski Naroden Sǎjuz"; "BZNS") is a political party devoted to representing the causes of the Bulgarian peasantry.  It was an agrarian movement and was most powerful between 1900 and 1923.  Unlike the socialist movements of the early 20th century, it was devoted to questions concerning agriculture and farm workers, rather than industry and factory workers.  The BZNS, one of the first and most powerful of the agrarian parties in Eastern Europe, dominated Bulgarian politics during the beginning of the 20th century.  It is also the only agrarian party in Europe that ever came to power with a majority government, rather than merely as part of a coalition.  It is a founding member of the former International Agrarian Bureau.

Finnish presidential election, 1931: Two-stage presidential elections were held in Finland in 1931.  On 15 and 16 January the public elected presidential electors to an electoral college.  They in turn elected the President.  The result was a victory for Pehr Evind Svinhufvud, who won on the third ballot by just two votes.  The turnout for the popular vote was 47.3%.  This presidential election was held during an ideologically, politically, socially and economically tense time.  The Great Depression was impoverishing many Finnish farmers and workers.  The far-right Lapua Movement had not settled for the ban of the Communist Party and its affiliated organizations in the autumn of 1930.  It wanted to help elect a President who would also strongly oppose the Social Democrats and moderate bourgeois parties, such as the Progressives.  Although Svinhufvud disapproved of the Lapua Movement's violent kidnappings of left-wing politicians and other illegal acts, he was their preferred presidential candidate.  Former President K.J. Ståhlberg, a champion of democracy, parliamentarism and the rule of law, had been briefly kidnapped by some activists of the Lapua Movement with his wife in October 1930.  He was chosen as the Progressive presidential candidate.  Speaker of the Finnish Parliament, Kyösti Kallio, held ideals similar to those of Ståhlberg, and he became the Agrarian presidential candidate.  The outgoing President, Lauri Kristian Relander, had lost the Agrarian presidential candidacy to Kallio, because he did not condemn the Lapua Movement as strongly as Kallio did, and a sufficient number of Agrarians believed that Kallio could control the Lapua Movement's extremists more effectively than Relander.  Right-wing Finns and some centrists, such as a prominent Agrarian parliamentarian, Juho Niukkanen, were concerned that Ståhlberg's re-election (after a six-year break) as the Finnish President would escalate political tensions in Finland.  The Commander-in-Chief of the Civil Guards (a bourgeois voluntary defence organization), Major General Lauri Malmberg, announced in the Finnish Parliament that he would not guarantee order among the Civil Guards, if Ståhlberg was elected President.  Svinhufvud's razor-thin victory required Niukkanen's arm-twisting tactics, whereby he pressured all the Agrarian presidential electors to support Svinhufvud.  This 69-year-old and slightly ailing conservative politician was considered by his supporters as a sufficiently bold, solid and patriotic man to re-unite the ideologically divided Finns.  His pro-democracy supporters hoped that he could keep both right-wing extremists and left-wing extremists in check (see, for example, Sakari Virkkunen, Finland's Presidents I / Suomen presidentit I. Helsinki: Otava Ltd., 1994, pgs.  242-245 (Relander), pgs.  11-14 (Svinhufvud); Pentti Virrankoski, A History of Finland / Suomen historia, volumes 1&2.  Helsinki: Finnish Literature Society / Suomalaisen kirjallisuuden seura, 2009, pgs.  810-816; Raimo Salokangas, "The Independent Republic" (Itsenäinen tasavalta), pgs.  635-639 in Seppo Zetterberg et al., eds., A Small Giant of the Finnish History / Suomen historian pikkujättiläinen.  Helsinki: WSOY, 2003).

Eufemio Zapata: Eufemio Zapata Salazar (1873, Ciudad Ayala - June 18, 1917, Cuautla, Morelos) was a participant in the Mexican Revolution and the brother of Mexican revolutionary Emiliano Zapata.  He was known as a womanizer, a macho man, and a very heavy drinker.

Emiliano Zapata: Emiliano Zapata Salazar (] ; 8 August 1879 – 10 April 1919) was a leading figure in the Mexican Revolution, the main leader of the peasant revolution in the state of Morelos, and the inspiration of the agrarian movement called "Zapatismo".

Kim Yong-ki: Kim Yong-ki (1908–1988) was a South Korean agrarian movement leader, Christian and philosopher.  He was a pioneer in waste land cultivation, and strove to demonstrate through his work that life as a farmer can be fulfilling and productive.  His mission was to induce dynamic spiritual, inspirational, and economic change in rural areas of South Korea.  He is considered one of the founding fathers of the New Community Movement, the foundation of South Korea's modernization.  He founded the Canaan School in Gwangju, Gyeonggi, in 1962.  In recognition of his work, he was awarded the Ramon Magsaysay Award for Public service in 1966.

Peng Pai: Peng Pai ( ) (October 22, 1896 – August 30, 1929) born in Haifeng County (now under Shanwei Municipality), Guangdong Province, China, was a pioneer of the Chinese agrarian movement and peasants' rights activist, a prominent revolutionary, and one of the leaders of Chinese Communist Party (CCP) at its earlier stage.  Peng Pai was one of the few Chinese intellectuals who were aware in early 1920s that peasantry and land issues caused the most critical problems for Chinese society.  He believed that the success of any revolution in China must depend on the peasants as its base foundation.

Revolutionary Agrarian Movement of the Bolivian Peasantry: Revolutionary Agrarian Movement of the Bolivian Peasantry

Zapata (lithograph): Zapata (1932) is a lithograph by the Mexican artist Diego Rivera (1886–1957) that depicts the Mexican revolutionary Emiliano Zapata (1879–1919) as he holds the reins of a horse among a group of "campesinos" (peasants).  The lithographic edition was created and printed twelve years after Zapata's assassination.  Zapata is based on Agrarian Leader Zapata (1931), one of eight "portable" frescoes produced explicitly for Rivera's solo exhibition at the Museum of Modern Art (MoMA) in 1931, which was adapted from his previous "Revolt" panel from a fresco titled "The History of Cuernavaca and Morelos" (1929–30) painted in the Palace of Cortés, Cuernavaca.  There were 100 original prints of the lithograph, many of which are in the collections of various art museums.

Progressive Party of Manitoba: The Progressive Party of Manitoba, Canada, was a political party that developed from the United Farmers of Manitoba (UFM), an agrarian movement that became politically active following World War I.  A successor to the Manitoba Grain Growers' Association, the UFM represented the interests of farmers frustrated with traditional political parties.

Question: Eufemio Zapata's brother was the inspirtion for what agrarian movement?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "eufemio_zapatas_brother": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of Eufemio Zapata's brother."
        },
        "role_in_revolution": {
          "type": "string",
          "description": "The brother's role in the Mexican Revolution."
        }
      },
      "required": [
        "name",
        "role_in_revolution"
      ],
      "additionalProperties": false
    },
    "agrarian_movement": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the agrarian movement inspired by Emiliano Zapata."
        },
        "inspiration_source": {
          "type": "string",
          "description": "The person who inspired the agrarian movement."
        }
      },
      "required": [
        "name",
        "inspiration_source"
      ],
      "additionalProperties": false
    },
    "movement_description": {
      "type": "string",
      "description": "A brief description of the agrarian movement."
    }
  },
  "required": [
    "eufemio_zapatas_brother",
    "agrarian_movement",
    "movement_description"
  ],
  "additionalProperties": false
}
