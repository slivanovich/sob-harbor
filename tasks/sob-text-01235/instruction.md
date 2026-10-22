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
Eye of the Leopard: Eye Of The Leopard, is a 2006 nature documentary film by National Geographic Channel that shows the journey, life, and growth of a young leopard cub named "Legadema".  The film is narrated by Jeremy Irons, who also voiced Scar in Disney's 1994 animated film "The Lion King".  Irons would later narrate "The Last Lions", a 2011 National Geographic documentary film.

The Mangler Reborn: The Mangler Reborn is a 2005 American horror film and the third entry in the "Mangler" film series based on a short story by Stephen King.  The movie was released straight to DVD on November 29, 2005 by Lions Gate Entertainment and Baseline StudioSystems.  Directors Gardner and Cunningham intended the film to be a "rebirth" of the film franchise, with the film not requiring viewers to have seen the prior two films.

Koyaanisqatsi: Koyaanisqatsi ( ), also known as Koyaanisqatsi: Life Out of Balance, is a 1982 American experimental film directed by Godfrey Reggio with music composed by Philip Glass and cinematography by Ron Fricke.

Mr. Bean Rides Again: "Mr. Bean Rides Again" is the sixth episode of the television series "Mr. Bean", and consists of two small stories, the first consisting of two sketches, the second consisting of three.  It was the last episode to credit both John Birkin and Paul Weiland as directors, as the former was later credited for all videotape scenes and the latter credited for all film scenes, while it was also the last to feature the episode title in the opening credits, as later episodes would display the episode's title after this on the first scene.  In addition, later episodes after this would only credit Robin Driscoll and Rowan Atkinson as co-writers of the programme.  The episode was originally aired on ITV on 17 February 1992.

Peter Berg: Peter Berg (born March 11, 1964) is an American director, actor, producer, and writer of film, television, and music videos.  His directorial film works include the black comedy "Very Bad Things" (1998), the action comedy "The Rundown" (2003), the sports drama "Friday Night Lights" (2004), the action thriller "The Kingdom" (2007), the superhero comedy-drama "Hancock" (2008), the military science fiction war film "Battleship" (2012), the war film "Lone Survivor" (2013), the disaster drama "Deepwater Horizon" (2016), and the Boston Marathon bombing drama "Patriots Day" (2016), the latter three all starring Mark Wahlberg.  In addition to cameo appearances in the last six of these titles, he has had prominent acting roles in films including "Cop Land" (1997), "Corky Romano" (2001), "Collateral" (2004), "Smokin' Aces" (2006) and "Lions for Lambs" (2007).

Seoul International Women's Film Festival: SEOUL International Women’s Film Festival (SIWFF, previously International Women's Film Festival in Seoul, IWFFIS) first took place on April 1, 1997, which marked the second appearance of the international film festival in Korea following Busan International Film Festival launched in 1996.  This was the time when there was no clear idea about how to define a film festival.  At that time, SEOUL International Women’s Film Festival came up with a catchphrase See the world through women’s eyes, setting its main goal to introduce women’s films that explore the “women’s reality from the women’s perspectives”.  Featuring films by women, for women, and of women, the 1st edition of SEOUL International Film Festival received a number of positive reviews from the audience, which was never anticipated this much.  Thanks to continuous support from the audience, SEOUL International Film Festival that used to be happening every other year has become an annual event since the 3rd edition in 2001.  For the 6th edition in 2004, SEOUL International Women’s Film Festival looked for changes by relocating the festival office and venues to Sinchon, the street of youth and culture.  For the 9th edition in 2007, the Queer Rainbow section was first introduced, presenting films about life and culture of gender minorities.  In order to go beyond the gender boundaries based on biological sex and to reach out for solidarity, SEOUL International Women’s Film Festival newly created the Open Cinema section encompassing feminist films made by male directors.  Now in 2015, SEOUL International Film Festival attempts to build its new festival identity and become a cultural platform more approachable for a wide variety of audiences by changing the official English title of the festival from International Women’s Film Festival in Seoul to SEOUL International Women’s Film Festival as well as by retouching the festival logo used for last 17 years.

The Last Lions: The Last Lions is a 2011 African nature documentary film by National Geographic Society, videotaped and directed by Dereck and Beverly Joubert.  It was shot at the Okavango Delta in Botswana.  The film premiered at the Palm Springs International Film Festival in January 2011 and was released in select theaters on February 18, 2011.  The film follows in the tradition of other National Geographic big cat films, such as "India: Land of the Tiger" and "Eye of the Leopard".

1993 British Lions tour to New Zealand: In 1993 the British Lions rugby union team toured New Zealand.  This tour followed the Lions' 1989 tour to Australia and preceded their 1997 tour to South Africa.  It was the last Lions tour in the sport's amateur era.

Richard Farmer (director): Richard Farmer is an award-winning film, commercial and music video director.  His directorial work has been shown in film festivals around the world, including the Saatchi & Saatchi New Directors' Showcase at Cannes Lions, and has garnered multiple MTV Video Music Awards and Best Short Film awards at both the Malibu International Film Festival and the BFI London Film Festival.

Garth Davis: Garth Davis is an Australian television, film and commercial director, best known for directing episodes of the series "Top of the Lake" (2013), for which he received Emmy and BAFTA nominations.  In 2008, he won a Gold Lion at the Cannes Lions International Festival of Creativity and a D&AD Pencil for Schweppes ‘Burst’ and in 2010 he received a finalist nomination in Directors Guild of America for best commercials director.

Question: Which film has more directors, Koyaanisqatsi or The Last Lions?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string"
          },
          "directors": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "director_count": {
            "type": "integer"
          }
        },
        "required": [
          "film_title",
          "directors",
          "director_count"
        ],
        "additionalProperties": false
      }
    },
    "film_with_more_directors": {
      "type": "string"
    },
    "max_director_count": {
      "type": "integer"
    }
  },
  "required": [
    "film_comparison",
    "film_with_more_directors",
    "max_director_count"
  ],
  "additionalProperties": false
}
