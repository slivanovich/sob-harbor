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
Wolfpac: Wolfpac (stylized as WOLFPAC) is an American hip hop group formed in 1997 by former Bloodhound Gang member and co-founder Daddy Long Legs.  The group's musical style fuses hip hop beats with hardcore and metal samples.  Its lyrical style draws from horrorcore, focusing on subjects such as resurrection, revenge, necrophilia, and standing up for one's own beliefs.  The group's live performances from time to time include a DJ, guitar player and strippers.

Pee Froiss: Pee Froiss is a hip hop group formed in Dakar, Senegal in 1993.  It was originally produced by another hip hop group from that city, Positive Black Soul, and since recorded with the duo.  The band's music is rapped in Wolof, French, and English and features traditional Senegalese instruments such as the kora as part of its instrumentation.  Pee Froiss was one of the first rap groups to include a female performer in their lineup, Sista Joyce.  The group's members create all of their own music videos with very sparse resources, the first of which was released in 1996 with their first album.

Crime Life: Gang Wars: Crime Life: Gang Wars is a video game released for Microsoft Windows, PlayStation 2 and Xbox.  The game is a fictionalized simulation of gang wars, with the game play focused on street fights involving many gang members at once.  Weapons include baseball bats, lead pipes, hammers and guns.  The game includes over 25 story-mode missions, as well as some free-play missions.  Free roam is also available as in the popular Grand Theft Auto.  The areas are relatively small but can prove useful when trying to locate your fellow gang members.  The game features harsh language and violence is definitely a staple of it.  The game's music is all hip-hop, reflecting the urban and hip-hop atmosphere of the game.  There are various methods of earning money, ranging from mugging to burglaries.  The soundtrack of the game is provided by the hip-hop group D12, which also contributed the likenesses and voices for some of the game's key characters.

Re-Up Gang: The Re-Up Gang are an American hip hop group formed in 2004, in Virginia Beach, Virginia.  The group was formed by Pusha T and Malice, brothers and members of Virginia-based hip hop duo Clipse, alongside Philadelphia-based rappers Ab-Liva and Sandman.  The Re-Up Gang is perhaps best known for their signature "We Got It 4 Cheap" mixtape series.

D12: D12, an initialism for The Dirty Dozen, is an American hip hop group from Detroit, Michigan.  D12 has had chart-topping albums in the United States, United Kingdom, and Australia.  D12 was formed in 1996, and achieved mainstream success after Eminem rose to international fame.  The original lineup consisted of the members and their alter egos.  This is where Slim Shady came from.  D12 released the album "Devil's Night" in 2001 and "D12 World" in 2004, spawning numerous hits such as "Fight Music", "Purple Pills", "My Band", "How Come" and "Shit on You" throughout that period.  Since 2006, Eminem's hiatus and the death of the member Proof resulted in them being less active in subsequent years.

Hudson Dusters: The Hudson Dusters was a New York City street gang during the early twentieth century.  Formed in the late 1890s by "Circular Jack", "Kid Yorke", and "Goo Goo Knox", the gang began operating from an apartment house on Hudson Street.  Knox, a former member of the Gopher Gang, had fled after a failed attempt to gain leadership of the gang from then leader, Marty Brennan.  However the two gangs later became allies during the gang wars against "Gay Nineties" gangs, the Potashes and Boodle Gangs, soon controlling most of Manhattan's West Side as far as 13th Street and eastern Broadway, bordering Paul Kelly's Five Points Gang to the north.  While the gang dominated the West Side, it constantly battled smaller rival gangs including the Fashion Plates, the Pearl Buttons, and the Marginals for control of the Hudson River docks throughout the 1900s.  Eventually, it drove the rival gangs out through sheer force of numbers, with over 200 members, not including the Gophers, who numbered several hundred more, controlling the waterfront by 1910.

Stetsasonic: Stetsasonic was an American hip hop group formed in 1981 in Brooklyn, New York City, New York.  It is remembered as one of the first hip hop crews to use a live band, and the group's positive, uplifting lyrics made it forerunners of alternative hip hop and jazz hip hop.

Sindicato Argentino del Hip Hop: Sindicato Argentino del Hip Hop is a hip hop group formed in Argentina.  They currently consist of three members: Smoler, DJ Fabry and Huexo , and two producers, but they have had different numbers of members over time .  Their style mainly consists of hip hop and funk.  The group received a Latin Grammy award in 2001 for best hip hop/rap album.

Blu (rapper): John Barnes III was born on April 15, 1983, in Los Angeles, California.  He was introduced to Hip Hop through his father, who gave him LL Cool J, Fat Boys, Kool Moe Dee, Ice-T, Too Short, 2 Pac, and Geto Boys tapes as a young kid.  His parents split when he was 6, and his stepfather was a pastor who restricted him from listening to hip hop and secular music.  He sang in the church choir and the choir in school.  His cousin wrote his first rap when he was 13, which they incorporated in their dance routines that they did all over the neighborhoods.  In High School, Blu moved to San Pedro where he began freestyle rapping in ciphers, making karaoke mixtapes, and battling rival crews.  He broke his ankle in 12th grade and dropped out shortly after he realized he would not be able to play basketball the rest of the season and many of his friends were killed in gang wars.  Blu kept rapping while maintaining odd jobs like selling shoes, warehouse work, and doing lights for movie sets.

Stypes: Stypes is an American Hip Hop Group formed late 2002 in Berwyn, Illinois, right outside of Chicago.  Originally formed as a two-piece Hardcore Hip Hop duo, Adam Mason, "StereoAdam" and Aaron Curran, "StereoAaron" appeared on many stages in the Chicago underground scene.  After doing shows with acts such as the Wu-Tang Clan, Crucial Conflict, and others, they achieved much local success with their 2006 song, "Berwyn".  The group helped spearhead the "Save The Spindle Campaign" to prevent the destruction of Dustin Shuler's seven car work of art called, The Spindle, located in Berwyn's Cermak Plaza.  Their attempt to rescue the sculpture was not enough yet their popularity continued to climb locally.  The release of the song, "Tock", on the 2008 album, "Nobody's Story", by Incise helped the once local act to stretch their sound over the pacific to Japan.  With the formation of a relationship with Kitchen Dip Recordings and the release of the album, "7 Stories High", in 2011 Stypes solidified their spot in the Chicago Hip Hop Scene.

Question: Crime  Life: Gang Wars, featured voices from what hip hop group formed in 1996?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_title": {
      "type": "string",
      "description": "The title of the video game."
    },
    "hip_hop_group": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the hip hop group."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the hip hop group was formed."
        }
      },
      "required": [
        "name",
        "formation_year"
      ],
      "additionalProperties": false
    },
    "contribution_details": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Details of the hip hop group's contribution to the game."
    }
  },
  "required": [
    "game_title",
    "hip_hop_group",
    "contribution_details"
  ],
  "additionalProperties": false
}
