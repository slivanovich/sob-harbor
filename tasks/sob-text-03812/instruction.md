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
Brenda Velez: Brenda Vélez (born March 23, 1979) is a Mexican Ballerina and Architect.  She is best known for performing in Swan Lake and in Giselle in Guadalajara's Teatro Degollado and owning VIA DANZA a dance academy in Guadalajara.

How It's Got to Be: "How It's Got to Be" is a song by German recording artist Jeanette.  Built around Russian composer Pyotr Ilyich Tchaikovsky's "Act 2, Scene 10: Moderato" from his ballet "Swan Lake" (1875–76), it was written by Biedermann and Kristina Bach and produced by Cobra for her second studio album "Delicious" (2001).  Released as the album's first single, it peaked at number seven on the German Singles Chart, reaching gold status.  In addition, it peaked at number 22 in Austria and Switzerland, respectively.

Ghislaine Thesmar: Ghislaine Thesmar (born 1943 in Beijing, China), a Ballerina, who studied at the Paris Conservatoire.  In 1968, she married the dancer and choreographer Pierre Lacotte.  Companies she danced with include Ballet du Marquis de Cuevas (1961), Lacotte's company, then the Paris Opera Ballet from 1972 to 1985; unusually, she joined the company directly as an "étoile" (principal).  She led the Ballets de Monte Carlo with Lacotte from 1986 to 1988.  She danced as a guest for the Rambert Ballet, the Grands Ballets Canadiens and the New York City Ballet.  She has taught for the Paris Opera Ballet.  She was frequently partnered by Michael Denard.  Her most celebrated roles include Odette/Odile in "Swan Lake" and Giselle in "Giselle".  The ballet film "La Sylphide" (1972) has been released twice on DVD/video and features Thesmar and Denard in the principal roles of the Sylph and the Scotsman, James.

Ruth Pryor: Ruth Pryor (1906-2001) was a Chicago ballet dancer and instructor, and the first American ballerina to dance the role of the Swan Queen in Swan Lake, in 1930.  She was known for "her feat of whirling thirty-six times a minute on her toes," according to the Purple Parrot of Northwestern University.

Swan Lake (Bourne): Matthew Bourne's "Swan Lake" was first staged at Sadler's Wells theatre in London in 1995.  The longest running ballet in London's West End and on Broadway, it has been performed in the UK, Los Angeles, Europe, Australia, South Korea, Japan, Israel and Singapore.  The story is based on the Russian romantic ballet "Swan Lake", from which it takes the music by Tchaikovsky and the broad outline of the plot.  Bourne's rendering is best known for having the traditionally female parts of the swans danced by men.

Tschaikovsky Pas de Deux: Tschaikovsky Pas de Deux is a ballet choreographed by George Balanchine to a composition by Pyotr Ilyich Tchaikovsky originally intended for act 3 of "Swan Lake" (op. 20, 1875-1876).  With costumes by Barbara Karinska and lighting by Jack Owen Brown, it was first presented by New York City Ballet at the City Center of Music and Drama, New York, on 29 March 1960.  Robert Irving conducted the New York City Ballet Orchestra.  The dancers were Violette Verdy and Conrad Ludlow.

Mann Center for the Performing Arts: The Mann Center for the Performing Arts (formerly known as the Mann Music Center) is a nonprofit performing arts center located in the Centennial District of Philadelphia's West Fairmount Park, built in 1976 as the summer home for the Philadelphia Orchestra.  It is the successor in this role to the Robin Hood Dell, where the Philadelphians have given summer performances since 1935.  It has since hosted numerous world-class artists and touring companies such as the American Ballet Theatre with Mikhail Baryshnikov, Marian Anderson, Leonard Bernstein, Buena Vista Social Club, Ray Charles, Judy Garland, the Metropolitan Opera, Mormon Tabernacle Choir, Paul Robeson, Itzhak Perlman, Lang Lang, Midori, and Yo-Yo Ma.  Major Philadelphia premieres have included the Israel Philharmonic Orchestra, Bolshoi Ballet and Orchestra’s production of Spartacus, and Britain’s Royal Ballet’s productions of Romeo and Juliet and Swan Lake.  Among the scores of award-winning popular artists presented by the Mann in recent years are Jack Johnson, Ed Sheeran, Phish, Tony Bennett, Mary J. Blige, Roger Daltrey, Bob Dylan, Furthur, Arcade Fire, Aretha Franklin, Herbie Hancock, Norah Jones, Diana Krall, Wynton Marsalis, Willie Nelson, Smokey Robinson, Jill Scott, James Taylor, Damien Rice, Alabama Shakes, Bon Iver, Lana Del Rey, The National, and Stevie Ray Vaughan.  In 2010, 2011 & 2014, the Mann was nominated by Pollstar, a concert industry trade publication, as "Best Major Outdoor Concert Venue" in North America.  The venue has a total seating capacity of approximately 14,000, with 4,743 seats under the roof and over 8,600 outside.

Swan Lake: Swan Lake (Russian: Лебединое озеро /"Lebedinoye ozero"), Op.  20, is a ballet composed by Pyotr Ilyich Tchaikovsky in 1875–76.  Despite its initial failure, it is now one of the most popular of all ballets.

Cynthia Harvey: Cynthia Harvey (born May 17, 1957) is an American dance teacher and former ballet dancer.  She was a principal dancer for the American Ballet Theatre.  Harvey was born in California, and joined American Ballet Theatre in 1974.  Her roles included Odette/Odile in "Swan Lake".  While Mikhail Baryshnikov was the artistic director at ABT, she performed as the prima ballerina in Baryshnikov's filmed production of "Don Quixote".

Sara Mearns: Sara Ann Mearns (born 19 January 1986) is an American ballerina who is a principal dancer with New York City Ballet.  She was born in Columbia, South Carolina, where she began dance training at the age of three.  As a teenager Mearns continued her studies with Patricia McBride and Stanislav Issaev, before entering the School of American Ballet in 2001.  She joined the New York City Ballet as an apprentice in 2003, and became a member of the corps de ballet in 2004.  She made her debut in a leading role just 18 months later in the dual roles of Odette/Odile in "Swan Lake" at the age of 19.  Mearns was promoted to soloist in 2006 and to principal in 2008.

Question: Brenda Vélez (born March 23, 1979), is a Mexican Ballerina and Architect, best known for performing in Swan Lake, a ballet composed by who in 1875–76?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ballet_name": {
      "type": "string",
      "description": "The name of the ballet."
    },
    "composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the composer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the composer."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "composition_years": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The starting year of the ballet's composition."
        },
        "end_year": {
          "type": "integer",
          "description": "The ending year of the ballet's composition."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "ballet_name",
    "composer",
    "composition_years"
  ],
  "additionalProperties": false
}
