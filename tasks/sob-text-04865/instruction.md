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
Bob Citron: Robert A. Citron, often called Bob Citron (September 14, 1932 – January 31, 2012) was an American entrepreneur and aerospace engineer who was born in Brooklyn, New York, and educated at the University of the Philippines (liberal arts) and aeronautical engineering from Northrop University (1953–1959).  Citron helped establish and manage the Smithsonian Astrophysical Observatory’s Moonwatch and Precision Optical Satellite Tracking Programs (STP) after the launch of Sputnik I in 1957.  He founded or co-founded five companies dealing with documentary film production (Limpopo Films Pty. Ltd. – 1964), publishing (Adventure Travel, Inc. – 1976), space research and space logistics support (SPACEHAB, Inc. – 1983), reusable satellite launch systems (Kistler Aerospace Corporation – 1993), and Lunar transportation and logistics (Lunar Transportation Systems, Inc. – 2004).  Citron also started three nonprofit foundations dealing with scientific field research (Educational Expeditions International with Clarence Truesdale, superintendent of Vermont public schools, in 1971, which became Earthwatch, short-lived phenomena (Center for Short-Lived Phenomena – 1975), and the study of the long-term future of humanity Foundation For the Future – 1996).  He died on January 31, 2012, at his home in Bellevue, Washington, at the age of 79, due to complications from prostate cancer.

George Eastman: George Eastman (July 12, 1854 – March 14, 1932) was an American entrepreneur who founded the Eastman Kodak Company and popularized the use of roll film, helping to bring photography to the mainstream.  Roll film was also the basis for the invention of motion picture film in 1888 by the world's first film-makers Eadweard Muybridge and Louis Le Prince, and a few years later by their followers Léon Bouly, William Dickson, Thomas Edison, the Lumière Brothers, and Georges Méliès.

Statens institut för rasbiologi: Statens institut för rasbiologi (SIFR, Swedish: "The State Institute for Racial Biology") was a Swedish governmental research institute founded in 1922 with the stated purpose of studying eugenics and human genetics.  It was located in Uppsala.  In 1958, it was renamed by the State Institute for Human Genetics ("Institutionen för medicinisk genetik") and is today incorporated as a department of Uppsala University.  Its first head was Herman Lundborg.

National Education Policy Center: The National Education Policy Center (NEPC) is a non-profit education policy research center located in the School of Education at the University of Colorado at Boulder.  It was founded in 2010 and is funded by a variety of governmental organizations, NGOs, and foundations.  The Center’s publications are intended for a broad audience that includes academic experts, policy makers, the media, and the general public.  The Center's goal is to provide high quality information in support of democratic deliberation about education policy.  Among its projects are the Think Tank Review project, the Commercialism in Education Research Unit, and the open access journal "Education Review".  The Center sponsors research, produces policy briefs, and publishes expert third party reviews of think tank reports.  NEPC will house a new Initiative on Diversity, Equity, and Learning (IDEAL), which is funded by the Ford Foundation.  NEPC is also the home of the Education Policy Alliance, a nationwide network of university-based research centers and organizations engaged in education policy research.

Centre national de la recherche scientifique: The French National Center for Scientific Research (French: "Centre national de la recherche scientifique" , CNRS) is the largest governmental research organisation in France and the largest fundamental science agency in Europe.  It employs 32,000 permanent employees (researchers, engineers, and administrative staff) and 6,000 temporary workers.

Peter Zandan: Peter A. Zandan (born 1953) is an American entrepreneur in the field of market research and data science.  Zandan is currently global vice chairman at Hill+Knowlton Strategies, where he leads the company’s worldwide research operations.  He was founder of IntelliQuest Information Group Inc., an Austin-based global research firm, and served as Chairman and CEO from 1984 to 1998, taking the company public in 1996.  Through IntelliQuest, Zandan pioneered the use of electronic surveys and the Internet in the field of market research.  In 1999, Zandan founded and served as CEO of Zilliant, a pricing optimization company.

William J. Tobin: William J. Tobin is an American entrepreneur, inventor, and business owner known for founding ten different startups since 1968, and securing 15 different patents for products and software.  Among the companies he founded and served as CEO and Director of Marketing are PC Flowers, Inc. from 1988, Instruments of Sweden, and Concept Industries, Inc.  He was named an "Entrepreneur of the Year" by "Inc.  Magazine" and in 2011 published the memoir and business tutorial "Confessions of a Compulsive Entrepreneur and Inventor".

Rudy A. Mazzocchi: Rudy A. Mazzocchi is an American entrepreneur and author.  In 1989 he founded the firm Microvena, which he built into a company valued at over $170 million.  After this he founded and then sold additional companies including Vascular Science, Inc., CytoGenesis, Inc. and Image-Guided Neurologics.  He is currently the CEO of Elenza, Executive Chairman of Establishment Labs Holdings, Inc. (ELHI), Executive Chairman of OptiStent, Inc. and Executive Chairman of LAFORGE Optical, Inc.  In 2012, published the award-winning novel "Equity of Evil".  He is the author of over 70 patents.

Research Institute of Petroleum Industry: The Research Institute of Petroleum Industry, also known as NIOC-RIPI, often shortened to RIPI (Persian: پژوهشگاه صنعت نفت‎ ‎ ) is a governmental research institute founded in 1959 in Tehran, Iran and is affiliated with National Iranian Oil Company.

Center for Governmental Research: The Center for Governmental Research, Inc. (CGR) is a non-profit corporation delivering data support, management consulting and implementation assistance to governments, educational institutions, foundations and non-profit organizations.  Headquartered in Rochester, New York, it was founded by George Eastman in 1915 as the Rochester Bureau of Municipal Research to provide research and guidance to its home city's government and community institutions.  Over the decades, CGR has grown from a bureau focused on the needs of one city into an organization with broader reach.  Today, CGR serves communities throughout the northeastern United States.  Its major practice areas are government management and education, public finance and economics, health and human services, and community data and information management.  It is an industry expert in working with communities on issues of municipal efficiency, economic and fiscal impact, public service delivery and local government restructuring, including evaluating the impacts of potential municipal consolidation.  It served as project manager for the 2013 municipal consolidation of Princeton, New Jersey, one of the largest municipal restructurings in New Jersey in almost a century. Via Governing Magazine It also developed the voter-approved plan in Seneca Falls, New York, resulting in the largest village dissolution in New York history.  Via CBS News

Question: When was the American entrepreneur died who founded The Center for Governmental Research, Inc?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entrepreneur_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entrepreneur."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the entrepreneur."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation or role of the individual."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the entrepreneur."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the entrepreneur."
        }
      },
      "required": [
        "name",
        "nationality",
        "occupation",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "founded_organization": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the organization founded by the entrepreneur."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the organization was founded."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "answer_death_date": {
      "type": "string",
      "description": "The specific death date of the entrepreneur who founded the organization, directly answering the question."
    }
  },
  "required": [
    "entrepreneur_details",
    "founded_organization",
    "answer_death_date"
  ],
  "additionalProperties": false
}
