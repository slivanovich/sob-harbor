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
L'amour toujours: "L'amour toujours" (also named "I'll Fly with You") is the title of a song co-written and recorded by the Italian DJ Gigi D'Agostino.  The song was released to American clubs and dance radio in July 2000.  In Europe, the song was released in October 2000.  The song is from the 1999 homonymous album.  In 2001, the song became extremely popular in the American dance club scene.  It became an international success and a huge hit throughout Europe, Latin America and Asia.  In the United States, it peaked at number 78 on the "Billboard" Hot 100 on September 15, 2001.

Another Way (Gigi D'Agostino song): "Another Way" is a song made by Italian "Pastore" DJ and Italo artist Gigi D'Agostino.  It was released in July 1999 as the fourth single from the album, "L'Amour Toujours".

Just Brothers: Just Brothers was the American musical duo of the brothers Jimmy and Frank Bryant and several session musicians.  Their song "Sliced Tomatoes" was a dancefloor hit in 1972, and was sampled in Fatboy Slim's "The Rockafeller Skank".

La Passion: "La Passion" is a song co-written and recorded by Italian DJ Gigi D'Agostino.  It was released in October 2000 as the sixth single from his 1999 album L'Amour Toujours.  It is a Remix with some additional melodic variations of the song "Rectangle" by the French musician Jacno, which doesn't originally contain any vocals.  Armenian singer and house music producer Andrew Sarkeesian provides the vocals, which were heavily auto-tuned, as were many songs which followed Cher's trend during the early 2000s.  D'Agostino has made various mixes for different albums.  The song was a hit in Austria and Belgium, where it became a number-one single.  It is notable that the words added to the French instrumental are a random blend of cliché like romantic lyrics with some gaga English as in the opening verse: "I never think you wanna, we won't belong, I can see your face too strong" followed by "I sing you wanna think you'll be wide on mind.  Don't you ever satisfy my soul in any by my side".  However, this perhaps has contributed to the song's success making it catchy, witty and easily sung and remembered even by non-singers and non-English speakers.

Super (1, 2, 3): "Super (1, 2, 3)" is a song made by Italian DJ Gigi D'Agostino in collaboration with disc jockey .  It was released in December 2000 as a single.

Bla Bla Bla: "Bla Bla Bla" is the title of a song written and recorded by Italian DJ Gigi D'Agostino.  It was released in May 1999 as the third single from the album, "L'Amour Toujours".  It reached number 3 in Austria and number 15 in France.  This song can also be heard in an added remixed mashup with "L'Amour Toujours (I'll Fly With You)" in its US radio version.  It was sampled in the song "Jump" from Lupe Fiasco's 2017 album Drogas Light.

Paper'd Up: "Paper'd Up" is a song by American West Coast hip hop recording artist Snoop Dogg, taken from his six studio album, "Paid tha Cost to Be da Bo$$" (2002).  It was produced by Fredwreck and features guest appearances by Kokane and Traci Nelson.  The beat, drum breaks and harmonies are heavily sampled from Dennis Edward's 1984 Disco Classic 'Don't Look Any Further' featuring Siedah Garrett.  The oriental vocal sample is from Ofra Haza's song Im Nin'alu.  This combination of sample material was already employed by Erik B. & Rakim in 1987 for their dancefloor classic Paid In Full, which was made famous by Coldcut 's Seven Minutes of Madness Remix.

Please, Please, Please, Let Me Get What I Want: "Please, Please, Please, Let Me Get What I Want" is a song originally performed by British group The Smiths.  It was released as the B-side of "William, It Was Really Nothing" in 1984 and later featured on the compilation albums "Hatful of Hollow" and "Louder Than Bombs".  The song has been covered by several artists, including The Decemberists, The Halo Benders, Franz Ferdinand, Elefant, OK Go, Deftones, Rob Dickinson, Emilie Autumn, Amanda Palmer, Hootie & the Blowfish, Muse, Cameo, Kaia Wilson, Third Eye Blind, Kate Walsh, The Dream Academy, Josh Rouse, She & Him, Slow Moving Millie, William Fitzsimmons and Sarah Darling, also, the chorus has been featured in a The Weeknd hook.  British band Clayhill have covered the song and their version can be heard at the end of the Shane Meadows film "This Is England".  Canadian electronic artist Venetian Snares also sampled the original song in "Nobody Really Understands Anybody".  Canadian PBR&B singer The Weeknd sampled the song's chorus for the bridge for his song "Enemy".  The song has become one of the most well known Smiths songs despite it only being a B-Side and it is often played by Morrissey during shows.

Dat Sexy Body: "Dat Sexy Body" is a song recorded by Jamaican deejay Sasha featuring Ivy Queen.  It was released in 1998, however didn't gain chart success until five years after being released.  The song was composed by Sasha, Queen, Ernesto Roberts and Anthony Kelly who also handled production of the song under his stage name Tony "CD" Kelly.  The song itself is recorded over a variation of the bookshelf riddim.  A music video for the song was also filmed.  A remix with Fatman Scoop was also recorded and released in 2004.  In 2016, the song was sampled in Zara Larsson's song "I Would Like" and in 2017, the song was sampled in Pitbull and Jennifer Lopez's song "Sexy Body".

Dream on the Dancefloor: "Dream on the Dancefloor" is a song by Swedish eurodance musician Basshunter, which appears on his fifth studio album, "Calling Time".  The song samples the main melody from Gigi D'Agostino's L'amour toujours.

Question: Which song was sampled in "Dream on the Dancefloor" and was recorded by Gigi D'Agostino?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sampled_song_title": {
      "type": "string",
      "description": "The title of the song that was sampled."
    },
    "sampled_song_artist": {
      "type": "string",
      "description": "The artist who recorded the sampled song."
    },
    "sampling_song_title": {
      "type": "string",
      "description": "The title of the song that performed the sampling."
    },
    "sampling_artist": {
      "type": "string",
      "description": "The artist who performed the song that did the sampling."
    }
  },
  "required": [
    "sampled_song_title",
    "sampled_song_artist",
    "sampling_song_title",
    "sampling_artist"
  ],
  "additionalProperties": false
}
