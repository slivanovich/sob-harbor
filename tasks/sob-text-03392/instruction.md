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
Jaime Zapata (painter): Jaime Zapata (26 November 1957) is an Ecuadorian painter.  He graduated from the Art Faculty of the School of Plastic Arts at the Universidad Central de Quito in 1972.

Stanfield Organization: On the fictional television drama "The Wire", the Stanfield Organization is a criminal organization led by Marlo Stanfield.  The Organization is introduced in Season Three of "The Wire" as a growing and significantly violent drug syndicate.  Marlo has established his organization's power in West Baltimore's main streets in the shadow of the dominating Barksdale Organization, which was more concerned with conducting its activities in the Franklin Terrace Towers.  The Stanfield Organization violently clashes with the Barksdale crew after the latter is forced to move on from the demolished Franklin Terrace Towers and tries to reclaim the streets the gang once dominated.  Marlo's is the only crew in the area not to let itself be absorbed into the feared Barksdale gang, and a violent turf war breaks out.  The Stanfield Organization begins as the underdog, but fallout from the strain of the war combined with a successful investigation by the Major Crimes Unit manages to destroy the Barksdale Organization at the end of Season Three.  By Season Four, Marlo's crew becomes the most powerful drug organization in West Baltimore, and forms an alliance with the New Day Co-Op while ruling its streets through fear.  In Season Five, after a period of aggressive expansion which culminates in Marlo seizing control of the Co-Op, a series of arrests and deaths destroy the organization.

Dark Circle: The Dark Circle is a fictional criminal organization in that appears in comic books from DC Comics, primarily part of the Legion of Super-Heroes comic books.  They first appeared in 1968, created by Jim Shooter as a criminal organization founded by five members and populated by a multitude of clones of the original five members.

Jaime Zapata: Jaime Jorge Zapata (May 7, 1978 – February 15, 2011) was an Immigration and Customs Enforcement, Homeland Security Investigations Special Agent who was ambushed and murdered by the Mexican criminal group Los Zetas in San Luis Potosí, Mexico.  He was one of the two agents that were ambushed in a part of the country that is increasingly under the influence of drug violence.  Zapata's death is the second highest-profile killing of a U.S. agent in Mexico—the first one was Enrique Camarena, an undercover DEA agent who was tortured and murdered by the former Guadalajara Cartel.

Texas State Highway Spur 260: Texas Spur 260, also known as Jaime Zapata Memorial Highway, is a state highway in southeastern Laredo, Texas connecting U.S. Route 83 and Texas State Highway 359.  The route was designated in 2008 but continued to be signed as part of Texas State Highway Loop 20 until the opening of Cuatro Vientos Road in July 2011, when the Loop 20 designation was shifted to the new route.  The contemporary Spur 260 constitutes the original extent of Loop 20, as originally designated in 1939.

Jaime González Durán: Jaime González Durán (a.k.a. "El Hummer") is a former Mexican drug lord who was one of the 31 original founding members and third-in-command of the criminal organization known as Los Zetas.  A former Mexican Army elite soldier of the Grupo Aeromóvil de Fuerzas Especiales (GAFE), he was trained in counter-insurgency and locating and apprehending drug cartel members.  He deserted in the late 1990s and was hired along with 30 other ex-soldiers by the Gulf Cartel leader, Osiel Cárdenas Guillen as his private enforcement army.

Sixth Family: A Sixth Family is an Italian-American or Italian-Canadian crime family or criminal organization that has become powerful or notable enough to rise to a level comparable or close to that of the Five Families of the New York City Italian-American Mafia.  A criminal organization deemed a "Sixth Family" may rival the Five Families or, alternatively, work closely enough with the Five Families that it appears to be a peer or near coequal of the families.

Jaime Zapata (disambiguation): Jaime Zapata (1978 –2011) was a U.S. ICE agent, killed in Mexico.

Los Zetas: Los Zetas (] , Spanish for "The Zs") is a Mexican criminal syndicate.  Considered by the US government to be "the most technologically advanced, sophisticated, efficient, violent, ruthless, and dangerous cartel operating in Mexico", the organization has expanded beyond the traditional purview of drug trafficking and also runs profitable sex trafficking and gun running rackets.  The origins of Los Zetas date back to the late 1990s when commandos of the Mexican Army deserted their ranks and began working as the enforcement arm of the Gulf Cartel.  In February 2010, Los Zetas broke away from their former employer and formed their own criminal organization.

Jaime Zapata (Labor Department spokesman): Jaime Zapata is a partner at GMMB, a public affairs marketing firm.  He was previously the Deputy Assistant Secretary for Public Affairs at the U.S. Department of Labor.

Question: When the group who murdered Jaime Zapata form their own criminal organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "criminal_organization_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the criminal organization."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the criminal organization formed."
        },
        "formation_month": {
          "type": "string",
          "description": "The month the criminal organization formed."
        }
      },
      "required": [
        "name",
        "formation_year",
        "formation_month"
      ],
      "additionalProperties": false
    },
    "victim_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the victim."
        },
        "agency": {
          "type": "string",
          "description": "The agency the victim worked for."
        }
      },
      "required": [
        "name",
        "agency"
      ],
      "additionalProperties": false
    },
    "event_type": {
      "type": "string",
      "description": "The type of event that occurred."
    }
  },
  "required": [
    "criminal_organization_details",
    "victim_details",
    "event_type"
  ],
  "additionalProperties": false
}
