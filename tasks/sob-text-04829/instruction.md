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
Bella Donna (album): Bella Donna is the debut studio album by American singer, songwriter and Fleetwood Mac vocalist Stevie Nicks.  Released on July 27, 1981, the album reached number one on the US "Billboard" charts in September of that year.  "Bella Donna" was awarded platinum status by the RIAA on October 7, 1981, less than three months after its release, and has since been certified quadruple-platinum.  "Bella Donna" spent nearly three years on the "Billboard" 200 from July 1981 to June 1984.  The album has sold over 6 million copies in the US alone with approximately a million copies since 1991 in the US according to Nielsen Soundscan.  It is Nicks' best-selling solo album to date.

Crystal Visions – The Very Best of Stevie Nicks: Crystal Visions... The Very Best of Stevie Nicks is a compilation album released by the American singer-songwriter and Fleetwood Mac vocalist Stevie Nicks.  It features songs from her solo career, as well as her career with Fleetwood Mac.  It includes her hit singles, a dance remix, and one new track, a live version of Led Zeppelin's "Rock and Roll".  Three singles were culled from the album: "Rock and Roll", "Landslide", and a remixed version of "Stand Back".  There are two versions of this album, one with just the audio CD and another version with an included DVD featuring all of Nicks' music videos with audio commentary from Nicks, as well as rare footage from the "Bella Donna" recording sessions.  The album debuted and peaked at #21 in the US selling 33,944 copies in its first week.  The album spent a total of 12 weeks on the "Billboard" 200 chart, and had sold 505,000 copies as of April 2014.  The album is certified gold in Australia and Silver in the UK.

Herbert W. Worthington: Herbert "Herbie" Wheeler Worthington lll (May 25, 1944 - November 2013), was an influential rock and roll photographer until his death at 69, in 2013.  He was best known as the photographer for Fleetwood Mac and Stevie Nicks (including the covers for her first two albums, "Bella Donna" and "The Wild Heart").  It was his photograph that was run on the cover of the Fleetwood Mac "Rumours" album and was instrumental in creating the iconic imagery (like the crystal ball) that is still associated with Fleetwood Mac today.  He photographed over 40 covers for several bands and artists, including Buddy Miles, Paris, Jesse Cutler 20/20 and Lita Ford, among many others, in his 30+ years as a rock music photographer.

Edge of Seventeen: "Edge of Seventeen" is a song by American singer-songwriter Stevie Nicks from her solo debut studio album "Bella Donna" (1981), released as the third single from "Bella Donna" on February 4, 1982.  The song was written by Nicks to express the grief resulting from the death of her uncle Jonathan and the murder of John Lennon during the same week of December 1980 and features a distinctive, chugging 16th-note guitar riff, and a simple chord structure typical of Nicks' songs.

Bella Donna (1923 film): Bella Donna is a 1923 American silent film produced by Famous Players-Lasky and released by Paramount Pictures.  The film is based on a novel, "Bella Donna", by Robert Smythe Hichens which was later adapted for a 1912 Broadway play starring Alla Nazimova.  This film is also a remake of the 1915 Paramount film "Bella Donna" starring Pauline Frederick.  The 1923 film was directed by George Fitzmaurice and starred Pola Negri in her first American film.

Bella Donna (comics): Bella Donna or Belladonna (from the Italian phrase "bella donna", or "beautiful woman") is a name or alias used by two fictional characters appearing in American comic books published by Marvel Comics.  One of these characters is Bella Donna Boudreaux, commonly associated with the X-Man Gambit.

Bella Donna (1915 film): Bella Donna was a 1915 American silent drama film produced by Famous Players-Lasky and the Charles Frohman Company, starring Pauline Frederick, and based on the play "Bella Donna" by James Bernard Fagan adapted from the novel of the same name by Robert Smythe Hichens.

Gambit (comics): Gambit (Remy Etienne LeBeau) is a fictional character appearing in American comic books published by Marvel Comics, commonly in association with the X-Men.  The character was created by writer Chris Claremont and artist Jim Lee.  Drawn by artist Mike Collins, Gambit makes his first appearances in "Uncanny X-Men Annual" #14 (July 1990) and "Uncanny X-Men" #266 (August 1990).

Stop Draggin' My Heart Around: "Stop Draggin' My Heart Around" was the first single from Stevie Nicks' debut solo album, "Bella Donna" (1981).  The track is the album's only song that was neither written nor co-written by Nicks.  Written by Tom Petty and Mike Campbell as a Tom Petty and the Heartbreakers song, Jimmy Iovine, who was also working for Stevie Nicks at the time, arranged for her to sing on it.  Petty sang with Nicks in the chorus and bridge, while his entire band (save Ron Blair, whose bass track was played by Donald "Duck" Dunn instead) played on the song.

Donna Windsor: Donna Windsor (also Windsor-Dingle) is a fictional character from the British ITV soap opera "Emmerdale".  She was originally played by Sophie Jeffery until 1997.  Actress Verity Rushworth took over the role in 1998.  She made her first appearance in the show on 26 August 1993.  It was reported on 8 April 2008 that Rushworth had quit the soap, as she wanted to avoid being "typecast", after being in the soap for a decade.  Donna departed on 30 January 2009.  At the time of her departure, Donna was the third longest running character on "Emmerdale".  It was announced on 8 January 2014 that Rushworth had decided to reprise her role as Donna for five months.  She returned on 19 March 2014 and it was revealed that Donna was terminally ill.  Donna committed suicide on 14 August 2014, after throwing herself and Gary North (Fergus O'Donnell) from a multi-storey car park to her death, but made her final appearance the following day, on 15 August.  Donna's funeral was held on 28 August 2014.

Question: What was the first appearance for the character that Bella Donna Boudreaux is commonly associated with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "associated_character_name": {
      "type": "string",
      "description": "The name of the character Bella Donna Boudreaux is associated with."
    },
    "associated_character_creators": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The writer and artist who created the associated character."
    },
    "first_appearance": {
      "type": "object",
      "properties": {
        "comic_title": {
          "type": "string",
          "description": "The title of the comic book where the character first appeared."
        },
        "issue_number": {
          "type": "string",
          "description": "The issue number of the comic book where the character first appeared."
        },
        "release_month": {
          "type": "string",
          "description": "The month of the comic book's release."
        },
        "release_year": {
          "type": "integer",
          "description": "The year of the comic book's release."
        }
      },
      "required": [
        "comic_title",
        "issue_number",
        "release_month",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "associated_character_name",
    "associated_character_creators",
    "first_appearance"
  ],
  "additionalProperties": false
}
