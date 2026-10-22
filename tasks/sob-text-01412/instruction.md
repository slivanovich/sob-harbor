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
Ettore Gracis: Ettore Gracis (24 September 1915 – 12 April 1992) was an Italian conductor.  Born in La Spezia, he studied at the Venice Conservatory and the Accademia Musicale Chigiana.  He became involved with the Venice Festival of Contemporary Music and the Naples Festival, conducting modern revivals of classical Italian and German operas (including Mozart and Rossini).  He spent much of his career at opera houses throughout Italy, including La Fenice, whose orchestra he led for twelve years.

Riccardo Massi: Riccardo Massi is an Italian operatic tenor who had performed at such Italian theatres as both the Giuseppe Verdi Theatre and La Scala.  He became known for his role as Mario Cavaradossi in "Tosca" which he performed in autumn of 2011 at the Bavarian State Opera and then performed again at the Berlin Opera Theatre in November of that year.  His US debut was in February 2012 as Radames in "Aida" at the Metropolitan Opera following by another summer performance that year.  In the autumn of 2012 he sang in "Il trovatore" staged by the Canadian Opera in Toronto and in February 2013 sang Calaf in "Turandot" produced by the Royal Swedish Opera.  He also became known for his performance as Don Alvaro in "La forza del destino" at the Australian Opera and the same year sang in another "Aida" production, this time at the Michigan Opera Theatre.  From 2013 to 2014 he performed at the Royal Opera House and as Cavaradossi at the Liceu in Barcelona.  Later on, he returned to Royal Swedish Opera where he sang the title role in "Andrea Chenier" and then another "Radames" at the Houston Grand Opera.  At the Opernhaus Zurich, he sang Calaf in December 2015.

Jane Rhodes: Jane Marie Andrée Rhodes (March 13, 1929 – May 7, 2011) was a French opera singer whose voice encompassed both the soprano and high mezzo-soprano ranges.  Her most celebrated role was Carmen, which she sang in the opera's first ever staging at the Palais Garnier.  She also created the roles of Isadora in Marcel Landowski's "Le Fou" and Maguelone in Georges Delerue's "Le Chevalier de Neige" and sang Renata in the first recorded performance of Prokofiev's "The Fiery Angel".  Admired for both her voice and her glamorous stage presence, she was nicknamed the "Bardot of the Opéra".  She was married to conductor Roberto Benzi.

Betty Jane Rhodes: Betty Jane Rhodes (April 21, 1921 – December 27, 2011) was an American actress and singer, most active in film during the late 1930s and the World War II era.  She was widely known to wartime movie audiences for her debut performance of the classic song, ""I Don't Want To Walk Without You"", in "Sweater Girl" in 1942.  In 2012, Tom Vallance of "The Independent" wrote of Rhodes performance, "Her place in the history of popular song is secured by her having introduced on screen one of the great songs of wartime longing, ""I Don't Want To Walk Without You"."

Twelfth Night: Twelfth Night, or What You Will is a comedy by William Shakespeare, believed to have been written around 1601–02 as a Twelfth Night's entertainment for the close of the Christmas season.  The play centres on the twins Viola and Sebastian, who are separated in a shipwreck.  Viola (who is disguised as Cesario) falls in love with Duke Orsino, who in turn is in love with the Countess Olivia.  Upon meeting Viola, Countess Olivia falls in love with her thinking she is a man.  The play expanded on the musical interludes and riotous disorder expected of the occasion, with plot elements drawn from the short story "Of Apollonius and Silla" by Barnabe Rich, based on a story by Matteo Bandello.  The first recorded performance was on 2 February 1602, at Candlemas, the formal end of Christmastide in the year's calendar.  The play was not published until its inclusion in the 1623 First Folio.

The Fiery Angel (opera): Sergei Prokofiev's opera, The Fiery Angel (Russian: Огненный ангел , "Ognenny angel" ), Op. 37, could be considered one of the composer’s largest challenges.  Writing, production, and location were all factors in the piece’s progress.  The journey to completion was not truly over until after Prokofiev’s time, when the piece was first presented in a full performance at the Théâtre des Champs-Élysées on 25 November 1955, and was first premiered at the Venice Festival in 1955.

The Christian Brothers Band (Memphis): The Christian Brothers Band of Christian Brothers High School (Memphis, Tennessee) is the oldest high school band in America, having a continuous existence since its founding in 1872.  The band was founded in the fall of 1872 by Br.  Maurelian, who served as the first band director.  The first recorded performance of the group was in the Memphis St. Patrick's Day Parade of 1873, and the band has performed every year since.  The band has an unbroken lineage of ten band directors.

Venice Festival of Contemporary Music: Venice Festival of Contemporary Music (Complete Italian name: "Festival Internazionale di Musica Contemporanea della Biennale di Venezia").  Founded in 1930 as an adjunct of the older Venice Biennale festival.  Some works by Prokofiev and Stravinsky were premiered at the festival.  Among composers featured in the first year were William Walton, Manuel De Falla, Zoltán Kodály, Ernest Bloch, Ferruccio Busoni, Arthur Honegger, and Paul Hindemith.  Excluding interruptions in World War II, the festival has continued to the present.

Sacro GRA: Sacro GRA (] , Italian for "Holy GRA") is a 2013 Italian documentary film directed by Gianfranco Rosi.  It won the Golden Lion at the 70th Venice International Film Festival.  It was the first documentary film to win the award at the Venice Festival.

Smoke Gets in Your Eyes: "Smoke Gets in Your Eyes" is a show tune written by American composer Jerome Kern and lyricist Otto Harbach for their 1933 musical "Roberta".  The song was sung in the original Broadway show by Tamara Drasin.  Its first recorded performance was by Gertrude Niesen, who recorded the song with orchestral direction from Ray Sinatra, Frank Sinatra's second cousin, on October 13, 1933.  Niesen's recording of the song was released by Victor, catalog# VE B 24454, with the B-side, "Jealousy", featuring Isham Jones and his Orchestra.

Question: The opera that Jane Rhodes sang Renata in the first recorded performance of was first performed at the Venice Festival in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opera_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the opera."
        },
        "composer": {
          "type": "string",
          "description": "The composer of the opera."
        }
      },
      "required": [
        "title",
        "composer"
      ],
      "additionalProperties": false
    },
    "premiere_information": {
      "type": "object",
      "properties": {
        "festival_name": {
          "type": "string",
          "description": "The name of the festival where the opera was first premiered."
        },
        "premiere_year": {
          "type": "integer",
          "description": "The year the opera was first premiered at the specified festival."
        }
      },
      "required": [
        "festival_name",
        "premiere_year"
      ],
      "additionalProperties": false
    },
    "answer_year": {
      "type": "integer",
      "description": "The final answer to the question: the year of the opera's premiere at the Venice Festival."
    }
  },
  "required": [
    "opera_details",
    "premiere_information",
    "answer_year"
  ],
  "additionalProperties": false
}
