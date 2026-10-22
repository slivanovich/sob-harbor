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
Nuttin' to Do: "Nuttin' to Do" / "Scary Movies" is the first single by hip hop duo Bad Meets Evil, composed of Detroit rappers Eminem and Royce da 5'9", released on October 1, 1999 by Game Recordings.  A year later, Bad Meets Evil would break up and Eminem would go on to work with D12 and Royce Da 5'9" would work on solo projects.  Royce took "Nuttin' to Do" for his album "Build and Destroy", and he also featured the sequel to "Scary Movies" as a solo song on it called "Scary Movies (The Sequel)".  "Scary Movies" was also featured on the soundtrack to the 2000 film "Scary Movie".

Royce da 5'9&quot;: Ryan Daniel Montgomery (born July 5, 1977), better known by his stage name Royce da 5′9″, is an American rapper from Detroit, Michigan.  He is best known for his longtime association with Eminem as well as his solo career, recording primarily with producers Carlos "6 July" Broady and DJ Premier, as well as ghostwriting for the likes of Diddy and Dr. Dre.  Royce is one half of the rap duo Bad Meets Evil with Eminem, one quarter of the hip hop group Slaughterhouse with Joe Budden, Joell Ortiz and Crooked I, and one half of the hip hop group PRhyme with DJ Premier.  The editors of About.com ranked him No. 30 on their list of the Top 50 MCs of Our Time (1987–2007).

Fast Lane (Bad Meets Evil song): "Fast Lane" is the lead single by hip hop duo Bad Meets Evil, a group composed of Royce da 5'9" and Eminem, from their first EP "".  The single was produced by Eminem, Supa Dups, and Jason "JG" Gilbert, and released on May 3, 2011 by Shady Records.  Texas rapper Chamillionaire released a remix.  A music video by director James Larese of music video direction group Syndrome.  The music video features animated visuals and kinetic typography, with cameo appearances by Mr. Porter and Slaughterhouse.  Fans and critics considered it a return to Eminem's Slim Shady alter ego.

Lighters (song): "Lighters" is a song by American hip hop duo Bad Meets Evil, a group composed of Royce da 5'9" and Eminem, from their first EP, "".  The track features American singer-songwriter Bruno Mars.  It was written by Bad Meets Evil, along with Mars, Philip Lawrence and Ari Levine of The Smeezingtons, and Roy Battle.  The production was handled by all aforementioned names, except Royce.  It was released on June 14, 2011 by Shady and Interscope Records, being later serviced to mainstream radio airplay in the United States by the two latter labels along with Aftermath Entertainment as the second single from the EP.  After writing and recording their own verses for the song, Eminem and Royce da 5'9" met Mars in Los Angeles, and the singer's vocals were added after minor adjustments were done by him and Eminem to the original cut.

Hell: The Sequel: Hell: The Sequel is the debut extended play (EP) by Bad Meets Evil, an American hip hop duo composed of Royce da 5'9" and Eminem.  It was released on June 13, 2011, in some countries, by Shady Records and Interscope Records and it was released on June 14, 2011 in the United States.  The EP is hardcore hip hop and midwest hip hop, and contains songs such as "Welcome 2 Hell", "Above the Law" and "Loud Noises" featuring Slaughterhouse; these tracks includes the violent lyrical content, while trying to maintain a humorous tone. " Fast Lane", "A Kiss" and "The Reunion" features the sexual themes.  "I'm on Everything" featuring Mike Epps, is a humorous song about drugs, while "Lighters" featuring Bruno Mars, and "Take from Me" features its focus on more serious themes such as success and music piracy.

Rock City (song): "Rock City" is a song by American rapper Royce da 5'9", released as the third single from his debut album, "Rock City (Version 2.0)", which was released in 2002 through E1 Music (formerly "Koch Records") and Game Recordings, after another record label had turned down his first version of the album.  The song also features vocals from rapper Eminem, becoming Eminem's debut appearance on one of Royce's solo albums.  The single was released on January 5, 2002, the same date as its same titled album was released.  "Rock City" charted at #99 on the Hot R&B/Hip-Hop Singles & Tracks chart in 2002.  Not counting Bad Meets Evil or Slaughterhouse songs, "Rock City" is Royce da 5'9"'s most successful single chart-wise.

Bad Meets Evil: Bad Meets Evil is an American hip hop duo composed of Detroit-based rappers, Royce da 5'9" (Bad) and Eminem (Evil).  Bad Meets Evil was formed in 1997, thanks to the duo's mutual friend, Proof.  Their discography consists of one extended play (EP) and four singles.  In 1999, the duo released a double non-album single, "Nuttin' to Do" and "Scary Movies"; the former peaked at 36 on the Hot Rap Songs chart, while the latter peaked at 63 on the UK Singles Chart, and was featured on the soundtrack of the 2000 horror comedy parody film "Scary Movie".

Jason Gilbert: Jason Gilbert, known by his nickname JG, is a Caymanian record producer and songwriter.  JG has produced for artists including Eminem, Bad Meets Evil, Akon, Christina Aguilera and Taio Cruz.

Sid Roams: Sid Roams is an American record production team composed of Joey Chavez and Tavish "Bravo" Graham.  Sid Roams have worked with several prominent artists, such as Eminem, Bad Meets Evil (Eminem and Royce da 5'9"), Prodigy of Mobb Deep, Evidence, Dilated Peoples, Infamous Mobb, Phil da Agony of Strong Arm Steady, Agallah, Chino XL and Lil' Fame of M.O.P., B.a.R.S. Murre, among others.  Sid Roams have released two instrumental albums, "Strctly Nstrmntl" (2008) and "Zombie Musik" (2009).

Proof (rapper): DeShaun Dupree Holton (October 2, 1973 – April 11, 2006), better known by his stage name Proof, was an American rapper and actor from Detroit, Michigan.  During his career, he was a member of the groups 5 Elementz, Funky Cowboys, Promatic, Goon Sqwad and most notably, D12.  He was a close childhood friend of rapper Eminem, who lived on the same block, and was often a hype man at his concerts.  In 2006, Proof was shot and killed during an altercation at the CCC nightclub in Detroit.

Question: Bad Meets Evil was a duo that formed because of a mutual friend from what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "duo_name": {
      "type": "string",
      "description": "The name of the hip hop duo."
    },
    "mutual_friend": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the mutual friend."
        },
        "origin_city": {
          "type": "string",
          "description": "The city the mutual friend is from."
        }
      },
      "required": [
        "name",
        "origin_city"
      ],
      "additionalProperties": false
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the duo was formed."
    }
  },
  "required": [
    "duo_name",
    "mutual_friend",
    "formation_year"
  ],
  "additionalProperties": false
}
