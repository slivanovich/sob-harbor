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
Gheorghe Dijmărescu: Gheorghe Dijmărescu (commonly known as George Dijmarescu) is a Romanian-American famous for escaping from the Romanian Dictator Nicolae Ceaușescu by swimming the Danube river, and for his mountaineering exploits including summiting Mount Everest multiple times in the early 2000s.  Gheorghe married Lhakpa Sherpa in 2002, the first Nepali woman to summit Mount Everest and survive and also the woman with most number of times to the summit of Mount Everest in the early 21st century.  They met in Kathmandu in the year 2000.  From 2008 he had some battles with medical problems.  Some of Dijmărescu's life was included in the Michael Kodas book "High Crimes", a book about a Mount Everest expedition in the early 2000s.  Dijmărescu organized a 2004 Connecticut expedition to Mount Everest.

Dicky Dolma: Dicky Dolma (born 5 April 1974) is an Indian woman who is known for being the youngest woman to summit Mount Everest up to that time at the age of 19 on May 10, 1993.  This occurred on the Indo-Nepal Women's Everest Expedition.  This Indo-Nepal Women's Everest Expedition was led by Bachendri Pal who was the first Indian woman to summit Mount Everest in 1984.  Dicky was also a skier and attended numerous sporting competitions including the 1989 All-India Open Auli Ski Festival and the Asian Winter Games in 1999.  She took ski training courses and basic mountaineering courses by the Manali Institute.  In the same expedition as Dicky Dolma, Santosh Yadav summited Mount Everest for the second time, the first woman to summit twice.  Dolma came from Palchan Village near Manali (in India).

Kharta: Kharta is a region in Tibet lying to the east of Mount Everest and centred on the Kharta valley and Kama valley.  The 40 km Kharta valley starts at the col at Lhakpa La at the head of the Kharta Glacier from which the Kharta Chu river flows east to join the Phung Chu just beyond Khata village.  Nearby to the south, the Kama valley starts at the Kangshung Glacier at the foot of Everest's Kangshung Face, and the Kama Chu flows southeast to the Phung Chu.  The 1921 British Mount Everest reconnaissance expedition discovered Kharta when reconnoitring ways to climb Mount Everest and managed to reach the North Col via the Lhakpa La.  Since that time Kharta has not been used as a way to approach the summit of Everest but the two valleys have become a popular area for trekking.

1924 British Mount Everest expedition: The 1924 British Mount Everest expedition was—after the 1922 British Mount Everest expedition—the second expedition with the goal of achieving the first ascent of Mount Everest.  After two summit attempts in which Edward Norton set a world altitude record of 28,126 feet (8572m), the mountaineers George Mallory and Andrew "Sandy" Irvine disappeared on the third attempt.  Their disappearance has given rise to the long-standing unanswered question of whether or not the pair climbed to the summit.  Mallory's body was found in 1999 at 26,760 feet (8155 m), but the resulting clues did not provide conclusive evidence as to whether the summit was reached.

The Private Life of the Gannets: The Private Life of the Gannets is a 1934 British short documentary film, directed by Julian Huxley, about a colony of Northern Gannet (Morus bassanus) on the small rocky island of Grassholm, off the coast of Wales.  It received a special mention at the 3rd Venice International Film Festival in 1935 and won the Best Short Subject (One-Reel) at the 10th Academy Awards in 1938.  The title was chosen by producer Alexander Korda as a reference to "The Private Life of Henry VIII" (1933), his breakthrough film of the previous year.

Mount Everest reconnaissance from Nepal: After World War II, with Tibet closing its borders and Nepal becoming considerably more open, Mount Everest reconnaissance from Nepal became possible for the first time culminating in the successful ascent of 1953.  In 1950 there was a highly informal trek to what was to become Everest Base Camp and photographs were taken of a possible route ahead.  Next year the 1951 British Mount Everest reconnaissance expedition reconnoitred various possible routes to Mount Everest from the south and the only one they considered feasible was the one via the Khumbu Icefall, Western Cwm and South Col.  In 1952, while the Swiss were making an attempt on the summit that nearly succeeded, the British practised their high-altitude Himalayan technique by attempting Cho Oyu, nearby to the west.

Erwin Emata: Erwin "Pastor" Emata (born 1973 in Davao City) is a mountain climber.  Based on The Himalayan Database  published by American Alpine Club , Erwin is the third Filipino to reach the peak of Mount Everest, the highest mountain in the world.  Like Leo Oracion, the second Filipino to reach Mount Everest's summit, he is a member of the First Philippine Mount Everest Expedition (FPMEE).  The Himalayan DataBase published by American Alpine Club had included Leo in the list of Everest South summitteers for 2006 on May 17, officially recognizing him as the 2nd Filipino on top Mount Everest.

Joint Himalayan Committee: The Mount Everest Committee was a body formed by the Alpine Club and the Royal Geographical Society to co-ordinate and finance the 1921 British Mount Everest reconnaissance expedition to Mount Everest and all subsequent British expeditions to climb the mountain until 1947.  It was then renamed the Joint Himalayan Committee; this latter committee organized and financed the successful first ascent of Mount Everest in 1953.

Douglas Douglas-Hamilton, 14th Duke of Hamilton: Air Commodore Douglas Douglas-Hamilton, 14th Duke of Hamilton and 11th Duke of Brandon (3 February 1903 – 30 March 1973) was a Scottish nobleman and pioneering aviator who, together with D.F. McIntyre, was the first man to fly over Mount Everest.

Wings Over Everest: Wings over Everest is a 1934 British short documentary film directed by Geoffrey Barkas and Ivor Montagu.  It won an Academy Award in 1936 for Best Short Subject (Novelty).  It described the 1933 Houston-Westland expedition, in which Douglas Douglas-Hamilton, 14th Duke of Hamilton, otherwise known as Lord Clydesdale, piloted a single-engined biplane on 3 April 1933, just clearing Everest's southern peak by a few feet, having been caught in a powerful downdraught.  The film used mixture of real footage of Everest from the record-breaking flight and theatrically produced scenes using the actual people rather than actors.

Question: What Scottish nobleman was the subject of a 1934 British short documentary and was the first man to fly over Mount Everest?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nobleman_name": {
      "type": "string",
      "description": "The name of the Scottish nobleman."
    },
    "full_title": {
      "type": "string",
      "description": "The full title of the nobleman."
    },
    "achievement": {
      "type": "string",
      "description": "The specific achievement related to Mount Everest."
    },
    "documentary_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the documentary."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the documentary."
        },
        "type": {
          "type": "string",
          "description": "The type of film (e.g., short documentary)."
        },
        "award": {
          "type": "string",
          "description": "An award received by the documentary."
        }
      },
      "required": [
        "title",
        "year",
        "type",
        "award"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "nobleman_name",
    "full_title",
    "achievement",
    "documentary_details"
  ],
  "additionalProperties": false
}
