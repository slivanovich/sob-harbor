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
Erwin Emata: Erwin "Pastor" Emata (born 1973 in Davao City) is a mountain climber.  Based on The Himalayan Database  published by American Alpine Club , Erwin is the third Filipino to reach the peak of Mount Everest, the highest mountain in the world.  Like Leo Oracion, the second Filipino to reach Mount Everest's summit, he is a member of the First Philippine Mount Everest Expedition (FPMEE).  The Himalayan DataBase published by American Alpine Club had included Leo in the list of Everest South summitteers for 2006 on May 17, officially recognizing him as the 2nd Filipino on top Mount Everest.

Mount Everest: Mount Everest, known in Nepali as Sagarmāthā and in Tibetan as Chomolungma, is Earth's highest mountain, located in the Mahalangur Himal sub-range of the Himalayas.  The international border between China (Tibet Autonomous Region) and Nepal runs across its summit point.

1922 British Mount Everest expedition: The 1922 British Mount Everest expedition was the first mountaineering expedition with the express aim of making the first ascent of Mount Everest.  This was also the first expedition that attempted to climb Everest using bottled oxygen.  The expedition would attempt to climb Everest from the northern side out of Tibet.  At the time, Everest could not be attempted from the south out of Nepal as the country was closed to Western foreigners.

Kabru: Kabru is a mountain in the Himalayas on the border of eastern Nepal and India.  It is part of a ridge that extends south from Kangchenjunga and is the southernmost 7000 m peak in the world.

1996 Mount Everest disaster: The 1996 Mount Everest disaster occurred on 10–11 May 1996, when eight people caught in a blizzard died on Mount Everest during attempts to descend from the summit.  Over the entire season, 12 people died trying to reach the summit, making it the deadliest day and year on Mount Everest before the 16 fatalities of the 2014 Mount Everest avalanche and the 18 deaths resulting from avalanches caused by the April 2015 Nepal earthquake.  The 1996 disaster gained wide publicity and raised questions about the commercialization of Everest.

Gheorghe Dijmărescu: Gheorghe Dijmărescu (commonly known as George Dijmarescu) is a Romanian-American famous for escaping from the Romanian Dictator Nicolae Ceaușescu by swimming the Danube river, and for his mountaineering exploits including summiting Mount Everest multiple times in the early 2000s.  Gheorghe married Lhakpa Sherpa in 2002, the first Nepali woman to summit Mount Everest and survive and also the woman with most number of times to the summit of Mount Everest in the early 21st century.  They met in Kathmandu in the year 2000.  From 2008 he had some battles with medical problems.  Some of Dijmărescu's life was included in the Michael Kodas book "High Crimes", a book about a Mount Everest expedition in the early 2000s.  Dijmărescu organized a 2004 Connecticut expedition to Mount Everest.

List of Mount Everest death statistics: List of Mount Everest death statistics is a list of statistics about death on Mount Everest.  For a list of mountaineering deaths on Mount Everest, see List of people who died climbing Mount Everest

Joint Himalayan Committee: The Mount Everest Committee was a body formed by the Alpine Club and the Royal Geographical Society to co-ordinate and finance the 1921 British Mount Everest reconnaissance expedition to Mount Everest and all subsequent British expeditions to climb the mountain until 1947.  It was then renamed the Joint Himalayan Committee; this latter committee organized and financed the successful first ascent of Mount Everest in 1953.

Dicky Dolma: Dicky Dolma (born 5 April 1974) is an Indian woman who is known for being the youngest woman to summit Mount Everest up to that time at the age of 19 on May 10, 1993.  This occurred on the Indo-Nepal Women's Everest Expedition.  This Indo-Nepal Women's Everest Expedition was led by Bachendri Pal who was the first Indian woman to summit Mount Everest in 1984.  Dicky was also a skier and attended numerous sporting competitions including the 1989 All-India Open Auli Ski Festival and the Asian Winter Games in 1999.  She took ski training courses and basic mountaineering courses by the Manali Institute.  In the same expedition as Dicky Dolma, Santosh Yadav summited Mount Everest for the second time, the first woman to summit twice.  Dolma came from Palchan Village near Manali (in India).

Mount Everest reconnaissance from Nepal: After World War II, with Tibet closing its borders and Nepal becoming considerably more open, Mount Everest reconnaissance from Nepal became possible for the first time culminating in the successful ascent of 1953.  In 1950 there was a highly informal trek to what was to become Everest Base Camp and photographs were taken of a possible route ahead.  Next year the 1951 British Mount Everest reconnaissance expedition reconnoitred various possible routes to Mount Everest from the south and the only one they considered feasible was the one via the Khumbu Icefall, Western Cwm and South Col.  In 1952, while the Swiss were making an attempt on the summit that nearly succeeded, the British practised their high-altitude Himalayan technique by attempting Cho Oyu, nearby to the west.

Question: Are Kabru and Mount Everest both on the border between Nepal and India?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked by the user."
    },
    "mountains_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the mountain."
          },
          "border_countries": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of countries that share a border with the mountain."
          }
        },
        "required": [
          "name",
          "border_countries"
        ],
        "additionalProperties": false
      },
      "description": "Details for each mountain being compared, including its border countries."
    },
    "are_borders_identical": {
      "type": "boolean",
      "description": "True if both mountains share the exact same set of border countries, false otherwise."
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the question (yes/no)."
    }
  },
  "required": [
    "question_asked",
    "mountains_compared",
    "are_borders_identical",
    "final_answer"
  ],
  "additionalProperties": false
}
