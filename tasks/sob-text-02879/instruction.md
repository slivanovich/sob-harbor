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
Elson Moyo: Air Vice-Marshal Elson Moyo was a deputy commander of the Air Force of Zimbabwe and one of the main figures in the 2007 Zimbabwean coup d'état attempt.

1997 Zambian coup d'état attempt: The 1997 Zambian coup d'état attempt was a military coup d'état attempt that took place in Zambia on 28 October 1997.  The coup lasted no more than 3 hours and took place between 6 and 9 A.M. when the coup's leader, Captain Solo (Stephen Lungu), announced via the national radio station (Zambia National Broadcasting Corporation) that a coup had taken place and that the then President, Frederick Chiluba, needed to step down.

2011 Bangladesh coup d'état attempt: 2011 Bangladesh coup d'état attempt was coup attempt in Bangladesh.  Bangladesh Army on December 2011 stopped a coup attempt that was planned to have taken place on the 11-12 of January 2012.  This was announced at a press conference on 19 January 2012.  The Purpose of the coup was to establish Islamic Law in Bangladesh.  A number of officers including retired ones were arrested.  The coup plotters argued that they are nationalist trying to prevent Bangladesh from being turned into a puppet of India.

2007 Zimbabwean coup d'état attempt: The Zimbabwean government foiled an alleged coup d'état attempt involving almost 400 soldiers and high-ranking members of the military that would have occurred on June 2 or June 15, 2007.  The alleged leaders of the coup, all of whom have been arrested and charged with treason, are retired army Captain Albert Matapo, Spokesman for the Zimbabwe National Army Ben Ncube, Major General Engelbert Rugeje, and Air Vice Marshal Elson Moyo.

2013 Libyan coup d'état attempt: The 2013 Libyan coup d'état attempt was a coup d'état attempt by a group of members of the General National Congress to take control of the country from Libyan Prime Minister Ali Zeidan.  Zeidan was kidnapped in the early hours of the 10 October by armed gunmen and was then released several hours later after a pro-government militia stormed the site where he was being held.  Following his release Zeidan claimed the incident was an attempted coup orchestrated by two militias in line with members of the GNC opposed to Zeidan.

1938 Greek coup d'état attempt: The Coup d'état attempt of 1938 or coup d'état of Chania was a short-lived coup attempt in Chania, Greece, aimed at overthrowing the dictatorship of Ioannis Metaxas in 1938.  Due to poor organization, the coup collapsed within a few hours and never seriously threatened the dictatorial regime.

1995 Azerbaijani coup d'état attempt: The 1995 Azerbaijani coup d'état attempt, also known as the Turkish coup in Baku, was a coup d'état attempt by members of the Azerbaijani military, led by Colonel Rovshan Javadov at the head of a unit of Special Purpose Police Unit ("OPON").  The group aimed to take control of the country from president Heydar Aliyev and reinstall former president Abulfaz Elchibey.  The coup was foiled when Turkish President Süleyman Demirel became aware of elements in Turkey supporting the plot, and called Aliyev to warn him.  On 17 March 1995, units of Azerbaijani Armed Forces surrounded the insurgents in their camp and assaulted it, killing Javadov.  Reports in Turkey following the 1996 Susurluk scandal elaborated on support for the coup from elements in Turkey.

1982 Spanish coup d'état attempt: The October 27, 1982, coup d'état attempt was a conspiracy conceived in Spain to overthrow the government.  Meant to take place on October 27, 1982, a day before national elections, the plan was discovered and foiled the preceding October 1.  Although made public, the importance of the coup attempt was downplayed with the cooperation of the main media, in order to avoid raising social unrest.  This coup d'état plan hardly affected the election campaign for the October 28 elections, won by Spanish Socialist Workers' Party (PSOE).  Over time, it has become an obscure chapter in Spanish history.

1989 Panamanian coup d'état attempt: The 1989 Panamanian coup d'état attempt was a failed coup d'état which occurred in Panama City on 3 October.  The attempt was led by Major Moisés Giroldi, supported by a group of officers who had returned from a United Nations peacekeeping mission in Namibia.  Although the plotters succeeded in capturing Panamanian dictator Manuel Noriega, the coup was quickly suppressed.  Giroldi, together with nine other members of the Panamanian Defense Forces, was executed on 3 and 4 October 1989.  An eleventh participant died in prison after being tortured.  These events became known as the "Albrook massacre".

1983 Upper Voltan coup d'état attempt: The 1983 Upper Voltan coup d'état attempt was an event which took place on 28 February 1983, in the Republic of Upper Volta (today Burkina Faso), just a few months after a previous "coup d'état" on 7 November 1982, carried out by radical elements of the army against the regime of Colonel Saye Zerbo, who himself came to power in a 1980 coup against Major General Sangoulé Lamizana.  The coup attempt on 28 February, which targeted the Council of Popular Salvation and its leader Major Dr. Jean-Baptiste Ouédraogo, failed.

Question: How is Elson Moyo associated to the 2007 Zimbabwean coup d'état attempt?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person involved."
    },
    "coup_attempt_year": {
      "type": "integer",
      "description": "The year the coup d'\u00e9tat attempt took place."
    },
    "country": {
      "type": "string",
      "description": "The country where the coup d'\u00e9tat attempt occurred."
    },
    "association_details": {
      "type": "object",
      "properties": {
        "primary_role": {
          "type": "string",
          "description": "The primary military or official role of the person."
        },
        "military_branch": {
          "type": "string",
          "description": "The military branch the person belonged to."
        },
        "involvement_description": {
          "type": "string",
          "description": "A description of the person's involvement in the coup attempt."
        },
        "outcome_status": {
          "type": "string",
          "description": "The status or outcome for the person following the coup attempt."
        }
      },
      "required": [
        "primary_role",
        "military_branch",
        "involvement_description",
        "outcome_status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "coup_attempt_year",
    "country",
    "association_details"
  ],
  "additionalProperties": false
}
