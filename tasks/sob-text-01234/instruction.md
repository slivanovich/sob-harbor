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
Hosoura Station: Hosoura Station (細浦駅 , Hosoura-eki ) was a JR East railway station located in Ōfunato, Iwate Prefecture, Japan.  The station, as well as most of the structures in the surrounding area, was destroyed by the 2011 Tōhoku earthquake and tsunami and has now been replaced by a provisional Bus Rapid Transit line.

2011 Tōhoku earthquake and tsunami: The 2011 earthquake off the Pacific coast of Tōhoku (東北地方太平洋沖地震 , Tōhoku-chihō Taiheiyō Oki Jishin ) was a magnitude 9.0–9.1 (M) undersea megathrust earthquake off the coast of Japan that occurred at 14:46 JST (05:46 UTC) on Friday 11 March 2011, with the epicentre approximately 70 km east of the Oshika Peninsula of Tōhoku and the hypocenter at an underwater depth of approximately 29 km .  The earthquake is often referred to in Japan as the Great East Japan Earthquake (東日本大震災 , Higashi nihon daishinsai ) and is also known as the 2011 Tōhoku earthquake, and the 3.11 earthquake.  It was the most powerful earthquake ever recorded in Japan, and the fourth most powerful earthquake in the world since modern record-keeping began in 1900.  The earthquake triggered powerful tsunami waves that reached heights of up to 40.5 m in Miyako in Tōhoku's Iwate Prefecture, and which, in the Sendai area, traveled up to 10 km inland.  The earthquake moved Honshu (the main island of Japan) 2.4 m east, shifted the Earth on its axis by estimates of between 10 cm and 25 cm , and generated infrasound waves detected in perturbations of the low-orbiting GOCE satellite.

Giralia: Giralia Station often referred to as Giralia is a pastoral lease that operates as a sheep station.

2016 Christchurch earthquake: An earthquake occurred in Christchurch on 14 February 2016 at 1:13 p.m. local time (00:13 UTC) and initially recorded as 5.9 on the Richter scale, but subsequently reviewed as 5.7.  Often referred to as the Valentine's Day earthquake, it was centred in the sea off New Brighton at a depth of 15 km .  It was the first large earthquake that the Christchurch area had experienced since May 2012, and it was part of the earthquake sequence that started with the 4 September 2010 Canterbury earthquake.

Cresswell Downs: Cresswell Downs Station often referred to as Cresswell Downs is a pastoral lease that operates as a cattle station in the Northern Territory.

Central Station Metro station: Central Station often referred to as Central is an underground station on the Tyne and Wear Metro in Newcastle upon Tyne, England.  It is located below Newcastle railway station, from which the Metro station gets its name.  The station is the third-busiest on the network after Monument and Haymarket.

Mallapunyah: Mallapunyah Springs Station often referred to as Mallapunyah is a pastoral lease that operates as a cattle station in the Northern Territory.

Auvergne Station: Auvergne Station often just referred to as Auvergne is a pastoral lease that operates as a cattle station in the Northern Territory of Australia.

Headingly Station: Headingly Station often just referred to as Headingly is a pastoral lease that operates as a cattle station.  It is located about 156 km south of Camooweal and 133 km west of Dajarra in Queensland.

Ashburton Downs: Ashburton Downs Station often referred to as Ashburton Downs is a pastoral lease that once operated as a sheep station and presently operates as a cattle station.

Question: What is the earthquake that destroyed Hosoura Station often referred to as in Japan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the station that was destroyed."
    },
    "destructive_event_name": {
      "type": "string",
      "description": "The general name of the event that caused the destruction."
    },
    "event_type": {
      "type": "string",
      "description": "The type of natural disaster that occurred."
    },
    "japanese_reference_name": {
      "type": "string",
      "description": "The name by which the destructive event is often referred to in Japan."
    }
  },
  "required": [
    "station_name",
    "destructive_event_name",
    "event_type",
    "japanese_reference_name"
  ],
  "additionalProperties": false
}
