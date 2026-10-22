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
Disney's Fantillusion: Disney's Fantillusion!  was a regularly scheduled night-time parade, created by Ron Logan, that performed nightly at Disneyland Park (Paris) during its Summer and Winter Seasons.  It features floats and live performers covered in thousands of electronically controlled lights and a synchronized soundtrack controlled by a Dual-tone multi-frequency signaling (DTMF) tone broadcast along the parade route.  The parade was originally created for Tokyo Disneyland where it ran for six years from 1995 - 2001.  An updated version of the Main Street Electrical Parade replaced Fantillusion at Tokyo Disneyland known as the .

A Christmas Fantasy Parade: The "A Christmas Fantasy Parade" is an annual parade presented at Disneyland Park in the Disneyland Resort in Anaheim, CA.  The parade is a holiday parade that runs (usually) from the weekend before Thanksgiving until the Sunday after New Years.  It debuted in during the 1994 Holiday Season, replacing the ""Very Merry Christmas Parade"."  The parade features several Christmas themed floats and a catchy soundtrack, along with favorite Disney characters such as Mickey, Minnie, Donald, Daisy, Pluto, Goofy, Clarabelle Cow, Elsa, Anna, Woody & Buzz Lightyear, Belle, Beast, Snow White and her Prince, Princess Aurora, Prince Phillip, Cinderella, Prince Charming, Ariel, Prince Eric, Winnie the Pooh, Tigger, Eeyore, and the Babes in Toyland soldiers.  Earlier versions of the parade included Scrooge McDuck, Roger Rabbit, Max Goof, characters from "Lilo & Stitch", "The Hunchback of Notre Dame", "Mulan", "Aladdin", and also young children.

Disneyland Park (Paris): Disneyland Park, originally Euro Disney, is a theme park found at Disneyland Paris in Marne-la-Vallée, France.  The park opened on 12 April 1992 as the first of the two parks built at the resort.  Designed and built by Walt Disney Imagineering, its layout and attractions are similar to Disneyland Park in Anaheim, California and Magic Kingdom at Walt Disney World in Bay Lake, Florida.  Spanning 56.656 ha (the second largest Disney park based on the original, after Shanghai Disneyland Park), it is dedicated to fairy tales and Disney characters.  In 2016, the park hosted approximately 8.4 million visitors, making it the most-visited theme park in Europe, and the 13th-most visited theme park in the world.

Walt Disney's Parade of Dreams: Walt Disney's Parade of Dreams premiered on May 5, 2005 as part of the Happiest Homecoming on Earth, celebrating the 50th anniversary of Disneyland in California.  Conceived by VP Parades and Spectaculars, Steve Davison, the parade celebrates the dreams of Disney characters and includes Disney characters such as Mickey, Minnie, Tinker Bell, Cinderella, Snow White, Simba, Alice and Mad Hatter, Pinocchio, Belle and Beast, Ariel, Donald, Goofy, and Pluto.  The parade includes eight floats which include Getaway to Dreams, Dream of Enchantment, Dream of Laughter, Dream of Another World, Dream of Imagination, Dream of Adventure, and Dreams Come True.  It closed in November 2008 before the Holidays at Disneyland.

Happiest Faces on Earth: The Happiest Faces on Earth was a series of photo collages around the Disneyland Resort to commemorate the 50th anniversary of Disneyland Park.  In summer and fall 2004, Disney encouraged guests to send in their family pictures from Disney vacations.  They could be turned in online, through the mail, and in special mailboxes located around the Disneyland Resort.  The pictures were then taken and used to create mosaics of Disney characters, attractions, and art.  The mosaics are located in Disneyland Park and Disney California Adventure Park.  There are kiosks on Main Street, U.S.A. where guests can find the location of their photos.

Main Street Electrical Parade: The Main Street Electrical Parade is a nighttime parade, created by Bob Jani and project director Ron Miziker, famous for its long run at Disneyland at the Disneyland Resort in California and Magic Kingdom at the Walt Disney World Resort in Florida.  It features floats and live performers covered in thousands of electronically controlled lights and a synchronized soundtrack triggered by radio control along key areas of the parade route.  The parade has also spun off several other versions that ran or continue to run at Disney parks around the world.  Currently, an updated version runs at Tokyo Disneyland as the "Tokyo Disneyland Electrical Parade: DreamLights".  In 2014, Hong Kong Disneyland premiered a spiritual successor to the Main Street Electrical Parade, the "Paint the Night Parade", which, like its predecessor, features "Baroque Hoedown" as its theme song.  An extended version of "Paint the Night" premiered at Disneyland on May 22, 2015 as part of the park's 60th anniversary celebration.

The Wonderful Thing About Tiggers: "The Wonderful Thing About Tiggers" is the theme song and personal anthem of Tigger, a fictional tiger from the children's book series Winnie-the-Pooh.  Although Tigger's birthday is believed to be in October 1928, the year that "The House at Pooh Corner" was first published, on Tigger-related merchandise, Disney often indicates Tigger's birth year as 1968, a reference to the first year that Tigger appeared in a Disney production, "Winnie the Pooh and the Blustery Day".  That was also the same instance when Tigger first sang this song.  The song is repeated in Disney's 1974 release "Winnie the Pooh and Tigger Too! ", The Many Adventures of Winnie the Pooh ride and then again in the 1977 release "The Many Adventures of Winnie the Pooh".  "The Wonderful Thing About Tiggers" opens up the 2000 release of "The Tigger Movie".  In 1974, Paul Winchell earned a Grammy for his rendition of the song.

Return to Pooh Corner: Return to Pooh Corner is a children's music album by soft rock singer Kenny Loggins.  Released in 1994, it features songs written by John Lennon, Rickie Lee Jones, Paul Simon and Jimmy Webb, along with several other traditional children's songs.  It was a successful album for Loggins, selling over 500,000 copies, and was nominated for a Grammy.  Loggins returned to Pooh Corner several years later with 2000's "More Songs from Pooh Corner".  The songs are described as "music for parents and children to enjoy together".  Loggins's album More Songs from Pooh Corner contains the song that he helped the Sherman Brothers to write for The Tigger Movie, which was called Your Heart Will Lead You Home.  Guest appearances are made by David Crosby and Graham Nash on "All the Pretty Little Ponies", Patti Austin on the "Neverland Medley" and Amy Grant and Gary Chapman on the title track (a rewritten version of "House at Pooh Corner", a song Loggins wrote in high school and had previously recorded with Jim Messina for their 1971 album "Sittin' In").

Tigger: Tigger is a fictional tiger character originally introduced in A. A. Milne's book "The House at Pooh Corner."  Like other Pooh characters, Tigger is based on one of Christopher Robin Milne's stuffed toy animals.  Tigger appears in the Disney cartoon versions of Winnie the Pooh and has also appeared in his own film.

Pixar Play Parade: Pixar Play Parade was a parade at Disney California Adventure.  The parade features floats and characters based on Disney·Pixar films such as "Monsters, Inc.", "The Incredibles", and "Toy Story".  In a first for Disney California Adventure, the floats feature small water jets that shoot water into the crowd of spectators (this parade effect was first introduced in 1993 for "Aladdin's Royal Caravan" at Disneyland).  The music used in the parade is derived from Hong Kong Disneyland's Mickey's WaterWorks Parade, both having the same tunes with changes in lyrics.

Question: The "A Christmas Fantasy Parade" is an annual parade presented at Disneyland Park in the Disneyland Resort in Anaheim, CA., their parade features several Christmas themed floats and a catchy soundtrack, along with favorite Disney characters such as Tigger, a fictional tiger character originally introduced in who's book "The House at Pooh Corner"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "parade_name": {
      "type": "string",
      "description": "The name of the parade."
    },
    "parade_location": {
      "type": "string",
      "description": "The location where the parade is presented."
    },
    "featured_character_origin": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the character featured in the parade."
        },
        "book_of_introduction": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the book where the character was originally introduced."
            },
            "author": {
              "type": "string",
              "description": "The author of the book where the character was originally introduced."
            }
          },
          "required": [
            "title",
            "author"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "character_name",
        "book_of_introduction"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "parade_name",
    "parade_location",
    "featured_character_origin"
  ],
  "additionalProperties": false
}
