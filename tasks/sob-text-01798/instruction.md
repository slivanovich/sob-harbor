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
Mil Pedazos: "Mil Pedazos" ("Thousand Pieces") is a song performed by Colombian singer-songwriter Juanes for his sixth studio album "Loco de Amor" (2014).  Written by the singer, and the member of the Mexican band Café Tacuba, Emmanuel Del Real, and produced by Juanes with the collaboration of Steve Lillywhite, Universal Music Latino released the song as the second single from "Loco de Amor" on March 7, 2014.

Sino (Café Tacuba album): Sino is the Latin Grammy winning sixth studio album by Mexican band Café Tacuba, released on October 9, 2007 in Mexico, Latin America and the United States.  The band has once again worked with award-winning Argentine music producer Gustavo Santaolalla.

El Objeto Antes Llamado Disco: El objeto Antes Llamado Disco is the seventh studio album released by Mexican band, Café Tacuba, on October 22, 2012.  In this album, the band has once again collaborated with award-winning Argentine music producer Gustavo Santaolalla.

Café Tacuba: Café Tacuba (stylized Café Tacvba) is a band from Ciudad Satélite, Mexico.  The group gained popularity in the early 1990s.  They were founded in 1989, before they had the current lineup of Rubén Isaac Albarrán Ortega (lead vocals, rhythm guitar), Emmanuel "Meme" del Real Díaz (keyboards, piano, programming, rhythm guitar, melodica, vocals), José Alfredo "Joselo" Rangel Arroyo (lead guitar, vocals), and Enrique "Quique" Rangel Arroyo: (bass guitar, electric upright bass, vocals), their friend Roberto Silva played the keyboards for a short period of time.  Mexican folk music player Alejandro Flores is considered the 5th "tacubo", as he has played the violin in almost every Café Tacvba concert since 1994.  Since the "Cuatro Caminos" World Tour, Luis "El Children" Ledezma has played the drums in every concert but is not considered an official member of the band.

Re (Café Tacuba album): Re is the second studio album by Mexican band Café Tacuba, released in 1994.  The album has been called "the equivalent of The Beatles "White Album" for the rock en español movement" by "The New York Times".  The name comes from the second syllable in Solfege, and from it being their second album.

Los Odio!: Los Odio!  is a Mexican rock band from Mexico City formed by musicians who were already important in the Mexican music scene.  The band is made up of the composer and producer Francisco Huidobro (lead vocals and rhythm/lead guitar) from the band Fobia; Jay de la Cueva (lead guitar), who participates in projects like Titán, Fobia, Victimas del Dr. Cerebro, and Moderatto; Tito Fuentes (support guitar) from Molotov; and Quique Rangel (bass guitar) from Café Tacuba; and Gabriel Bronfman el Queso (bass and lap steel guitar), who plays in Resorte and K'an and People Project.  Their first and self-titled album peaked at #74 in Mexican charts.

Tiempo Transcurrido: Tiempo Transcurrido ("Running Time") is Café Tacuba's first compilation album, released in 2001.  According to the band, it was released due to a contractual obligation, as the original contract signed with WEA Latina stated that they must release five albums, and with no new material, Tiempo Transcurrido dropped in music stores on August 21.  The album itself chronicles Café Tacuba's work in reverse order, starting with Revés (originally titled "13" on Revés/Yo Soy) and ending with "La Dos."  The only new song on this compilation is a live rendition of "El Baile Y El Salón."  The album cover is noted for referencing each of their four albums up to that point, with the debut album cover being reversed and superimposed over the other three album covers.

MTV Unplugged (Café Tacuba album): Unplugged Café Tacuba is a complete live album (ninth overall) that was recorded in 1995 and released in 2005 as a CD/ DVD combo by Mexican alternative rock group Café Tacvba.  Café Tacuba was the first Latin rock band to ever appear on "MTV Unplugged".  The live performance was recorded in 1995 and released on CD and DVD in 5.1 surround sound on June 7, 2005.  The MTV Unplugged album includes the selections "El Metro," "La Ingrata," "Esa Noche," "Una Manana," "Bar Tacuba," and others.

Gustavo Santaolalla: Gustavo Alfredo Santaolalla (born 19 August 1951) is an Argentine musician, film composer and producer.  He has won Academy Awards for Best Original Score in two consecutive years, for "Brokeback Mountain" in 2005, and "Babel" in 2006.  More recently, he composed the original score for the video game "The Last of Us", and the theme music for the Netflix series "Making a Murderer".

No Hay Nadie Como Tú: "No Hay Nadie Como Tú" (English: There's No One Like You ) is the first single by alternative-rap band Calle 13 taken from their third studio album "Los de Atrás Vienen Conmigo", released on October 7, 2008 by Sony BMG.  It features Mexican alternative rock group Café Tacuba.  The single is known for its mixture of different musical styles, typical of Calle 13's music.  It's a blend of latin pop with rock and dance music.  The song won the 2009 Latin Grammys for Record of the Year & Best Alternative Song.

Question: El objeto Antes Llamado Disco is the seventh studio album released by Mexican band, Café Tacuba, on October 22, 2012, in this album, the band has once again collaborated with award-winning Argentine music producer, musician, and film composer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "collaborator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the collaborator."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the collaborator."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles the collaborator holds."
        }
      },
      "required": [
        "name",
        "nationality",
        "roles"
      ],
      "additionalProperties": false
    },
    "collaboration_role": {
      "type": "string",
      "description": "The specific role of the collaborator for this album."
    }
  },
  "required": [
    "album_name",
    "band_name",
    "collaborator",
    "collaboration_role"
  ],
  "additionalProperties": false
}
