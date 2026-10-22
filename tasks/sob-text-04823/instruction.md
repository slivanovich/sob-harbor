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
The Days of the Commune: The Days of the Commune is a play by the twentieth-century German dramatist Bertolt Brecht.  It dramatises the rise and fall of the Paris Commune in 1871.  The play is an adaptation of the 1937 play "The Defeat" by the Norwegian poet and dramatist Nordahl Grieg.  Brecht's collaborator Margarete Steffin translated the play into German in 1938 and Brecht began working on his adaptation in 1947.  The process was driven by another Brecht collaborator, Ruth Berlau, who had introduced Brecht to Grieg in 1931.

Let No One Deceive You: Let No One Deceive You: Songs of Bertolt Brecht (or simply Let No One Deceive You) is an album by American folk and blues singer Dave Van Ronk and vocalist Frankie Armstrong, released in 1992.  It consists completely of songs by Bertolt Brecht.

Arthur Kutscher: Arthur Kutscher (July 17, 1878, Hannover - August 29, 1960, Munich) was a German historian of literature and researcher in drama.  Together with Max Herrmann he can be seen as a founding father of theatre studies in Germany.  He was a professor at Munich University, where he taught a famous seminar in theatre history.  Kutscher was a friend of the iconoclastic dramatist and cabaret-star Wedekind.  His work influenced many playwrights, poets, and directors.  His students included Bertolt Brecht (studied in 1917), Erwin Piscator (studied in 1913), Peter Hacks, Hanns Johst, Klabund, and Erich Mühsam.  Brecht's first full-length play, "Baal" (written 1918), was written in response to an argument in one of Kutscher's drama seminars.  While Kutscher was responsible for inspiring an admiration for Wedekind in the young Brecht, he was "bitterly critical" of Brecht's own early dramatic writings.

J. K. Rowling: Joanne Rowling, {'1': ", '2': ", '3': ", '4': "} ( ; born 31 July 1965), who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist and screenwriter who wrote the "Harry Potter" fantasy series.  The books have won multiple awards, and sold more than 400 million copies.  They have become the best-selling book series in history and been the basis for a series of films, over which Rowling had overall approval on the scripts and was a producer on the final films in the series.

Messingkauf Dialogues: The Messingkauf Dialogues (German: "Dialoge aus dem Messingkauf" ) is an incomplete theoretical work by the twentieth-century German theatre practitioner Bertolt Brecht.  John Willett translates "Der Messingkauf" as "Buying Brass".  According to one Brecht scholar "Brecht worked on [the Messingkauf] primarily during the late 1930s and early 1940s.  In Brecht’s words it contains, “a lot of theory in dialog form.”

Bertolt-Brecht-Literaturpreis: Bertolt-Brecht-Literaturpreis (English: "Bertolt Brecht Literature Prize" ) is a literary award in Augsburg, Germany, birthplace of Bertolt Brecht.  It has been awarded every three years since 1995.  With a prize of €15,000, it is considered one of the most prestigious literary awards in Germany.  It is awarded to writers and personalities "who have distinguished themselves through the critical analysis of the present day in their literary works."  The 2006 edition marked the 50th anniversary of the death of Brecht.

Baal (EP): Baal is an EP by David Bowie, comprising recordings of songs written for Bertolt Brecht’s play "Baal".  It is sometimes referred to as David Bowie in Bertolt Brecht’s Baal, as credited on the sleeve.

Coriolanus (Brecht): Coriolanus is an unfinished German adaptation by the modernist playwright Bertolt Brecht of the English 17th-century tragedy by William Shakespeare.  Brecht wrote it sometime between 1951 and 1953.  This adaptation reveals the influence of Mao Tse-tung on Brecht's social thought especially the idea of primary and secondary contradictions which Mao discussed in his treatise On Contradiction.  Brecht alluded to this text and discusses his development on the original and his ideas for its staging in an essay entitled "Study of the First Scene of Shakespeare's "Coriolanus"", which is written in the form of a dialogue with his collaborators at the Berliner Ensemble theatre company.  The play was first staged by Heinrich Koch at the Frankfurt Schauspielhaus theatre, where it opened on 22 September 1962.  It was later staged by the Berliner Ensemble in September 1964.  Ruth Berghaus became famous for her staging of the slaughter scenes in this production.  The play was published in an English translation by Ralph Manheim in volume nine of Brecht's "Collected Plays".

Bertolt Brecht: Eugen Berthold Friedrich "Bertolt" Brecht ( ; ] ; 10 February 1898 – 14 August 1956) was a German poet, playwright, and theatre director of the 20th century.  He made contributions to dramaturgy and theatrical production, the latter through the tours undertaken by the Berliner Ensemble – the post-war theatre company operated by Brecht and his wife, long-time collaborator and actress Helene Weigel.

The Tutor (Brecht): The Tutor is the 1950 adaptation, by 20th century German dramatist Bertolt Brecht, of an 18th-century play by Lenz.  The original Lenz play was produced in 1774 and is also known by the title "The Advantages of a Private Education".  Brecht contributed few additions to the plot of the original work, but made many cuts and alterations.  Brecht's work is two thirds the length of the original play and over half the material is new.  The play was Brecht's first production which featured work from the German Classical Era for the Berliner Ensemble.  Overall, it was the third production the Berliner Ensemble performed.  Brecht himself directed this production.  'The Tutor' was translated by Ralph Manheim and Wolfgang Sauerlander.

Question: Who was born first, J. K. Rowling, or Bertolt Brecht?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "earliest_born_person_name": {
      "type": "string"
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "person_a",
    "person_b",
    "earliest_born_person_name",
    "comparison_summary"
  ],
  "additionalProperties": false
}
