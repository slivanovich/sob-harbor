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
African Centre for Technology Studies: African Centre for Technology Studies (ACTS) is an intergovernmental non-profit organization, founded in 1988 by Calestous Juma {'1': ", '2': ", '3': ", '4': "} in Nairobi, Kenya, promoting policy-oriented research on science and technology in development that is sustainable in terms of the economy, society, and the environment.  It was the first African non-profit organization to combine policy research, science and technology.

Access Research Network: Access Research Network (ARN) is an American non-profit organization that reports on science, technology and society from an intelligent design perspective.  ARN primarily disseminates information via its website, located at ARN.org, which contains commentary, articles (both original and from other sources), videos, links, and a bookstore, all focusing on intelligent design.  Between 2006 and 2011, ARN also published an annual list of "Top 10 Darwin and Design News Stories" compiled by ARN staff and released at the end of each year.

Protected Harvest: Protected Harvest is an American non-profit organization headquartered in Soquel, California that certifies sustainably grown crops.  The goal of the organization is to provide a standard measurement of what constitutes a sustainable product and use it to assure retailers and consumers that they are pucharsing sustainably grown items.  Protected Harvest was founded in 2001 as an independent non-profit organization and merged into SureHarvest in 2008.  According to EcoLabeling.org, a non-profit monitoring certification programs, "Protected Harvest is an eco-label with the stated mission of helping farmers meet environmental standards that yield high quality products and preserve healthy land for future generations."  Pest-management in particular is among the specialties of Protected Harvest, according to Consumer Reports.

Mainstream Science on Intelligence: Mainstream Science on Intelligence was a public statement issued by a group of academic researchers in fields associated with intelligence testing that claimed to present those findings widely accepted in the expert community.  It was originally published in the "Wall Street Journal" on December 13, 1994 as a response to what the authors viewed as the inaccurate and misleading reports made by the media regarding academic consensus on the results of intelligence research in the wake of the appearance of "The Bell Curve" by Richard Herrnstein and Charles Murray earlier the same year.  It was drafted by professor of psychology Linda Gottfredson, sent to 131 researchers, and signed by 52 university professors specializing in intelligence and related fields, including around one third of the editorial board of the journal "Intelligence", in which it was subsequently reprinted in 1997.  The 1997 editorial prefaced a special volume of "Intelligence" with contributions from a wide array of psychologists.

Allen St. Pierre: Allen St. Pierre is the Executive Director of the National Organization for the Reform of Marijuana Laws (NORML), an American non-profit organization that wishes to remove the criminal penalties for and legalize cannabis.  St. Pierre was hired by NORML's Board of Directors in 1991 when he worked as a Communications Director for the organization.  He gradually rose through the ranks, becoming the Deputy National Director in 1993.  When the NORML Foundation was created in 1997, St. Pierre was chosen to be its Executive Director.  The NORML Foundation is a sister organization of NORML that works "to better educate the public about marijuana and marijuana policy options, and to assist victims of the current laws".

David M. Gilbert: David M. Gilbert is J. Herbert Taylor Distinguished Professor of Molecular Biology in the Department of Biological Science and Co-founder and Associate Director of the Center for Genomics and Personalized Medicine at Florida State University.  Gilbert’s work focuses on the mechanisms regulating DNA replication during the cell cycle and the relationship between DNA replication and structural and functional organization of chromosomes, most recently during differentiation in human and mouse embryonic stem cells and in pediatric leukemia.  Gilbert received his BA degrees in Biochemistry/Cell Biology and Philosophy from the University of California, San Diego and his PhD in Genetics from Stanford University.  He did two post-doctoral training periods, first as an EMBO Fellow with Pierre Chambon in Strasbourg, France, studying transcriptional control, and second as a Roche Fellow with Melvin DePamphilis studying replication origin recognition.  He joined the faculty at State University of New York (SUNY) Upstate Medical University in 1994 and was appointed full professor in 2003.  In 2006, he moved to Florida State University for his current endowed chair position and was elected as a fellow of the American Association for the Advancement of Science (AAAS) in 2008 and then elected as a council delegate of the AAAS in 2010, as well as to the American Society of Hematology in 2013 and the International Society for Stem Cell Research in 2014.  Gilbert’s other awards include the American Cancer Society Junior Faculty Research Award (2000), the SUNY President’s Young Investigator Award (2002), the NIH Career Enhancement Award for Stem Cell Research (2004) Florida State University Distinguished Research Professor (2015) and the Pfeiffer Endowed Professorship for Cancer Research (2015).  He is a principal investigator in the NIH Encyclopedia of DNA Elements (ENCODE) Consortium and is a board member of the Southeast Stem Cell Consortium (SESCC).  He has served on American Cancer Society (1996–2004) and NIH study sections (1997–present) and is an editorial member of the Epigenetics Society and is on the editorial board of the Journal of Cell Biology.  He also maintains ReplicationDomain, a free online database resource for storing, sharing and visualizing DNA replication timing and other chromosome mapping data.

From Darwin to Hitler: From Darwin to Hitler: evolutionary ethics, eugenics, and racism in Germany is a 2004 book by Richard Weikart, a historian at California State University, Stanislaus, and a senior fellow for the Center for Science and Culture of the Discovery Institute.  The work is controversial.  Graeme Gooday, John M. Lynch, Kenneth G. Wilson, and Constance K. Barsky wrote that "numerous reviews have accused Weikart of selectively viewing his rich primary material, ignoring political, social, psychological, and economic factors" that helped shape Nazi eugenics and racism.

Mark Alan Walker: Mark Alan Walker, Ph.D. is an Associate Professor of Philosophy at New Mexico State University, where he occupies the Richard L. Hedden Endowed Chair in Advanced Philosophical Studies.  Prior to his professorship at NMSU Prof. Walker taught at McMaster University in the department of philosophy and the Arts & Science Programme.  He is the author of "Happy-People Pills for All" (Oxford: Blackwell Press, 2013).  Walker founded and was president of the former nonprofit organization Permanent End International (2003–2007), which had been devoted to ending hunger, illiteracy and environmental degradation through the dissemination of modular aquaponics systems for farming.  He serves on the editorial board of the Journal of Evolution and Technology and on the board of directors of the Institute for Ethics and Emerging Technologies.  He is a former board member of the non-profit organization Humanity Plus (formerly World Transhumanist Association).

Richard Weikart: Richard Weikart (born July 1958) is a professor of history at California State University, Stanislaus, and is a senior fellow for the Center for Science and Culture of the Discovery Institute.  In 1997 he joined the editorial board of the Access Research Network's "Origins & Design Journal".  Weikart's work focuses on the impact of evolution, which he and the Discovery Institute term Darwinism, on social thought, ethics and morality.  His work and conclusions are controversial.

Society for Nutrition Education and Behavior: The Society for Nutrition Education and Behavior (SNEB) is an American non-profit organization that represents the professional interests of nutrition educators in the United States and worldwide.  The organization was founded as the Society for Nutrition Education in 1968 as a non-profit organization to publish the Journal of Nutrition Education.  Once the Journal was established the Society expanded its purposes to include education, communication and research activities.  The first issue of the Journal was published as Summer in 1969.

Question: in 1997, Richard Weikart joined the editorial board of an American non-profit organization that reports on science, technology, and society, from what perspective?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the non-profit organization."
    },
    "is_non_profit": {
      "type": "boolean",
      "description": "Indicates if the organization is a non-profit."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the organization is based."
    },
    "year_weikart_joined_board": {
      "type": "integer",
      "description": "The year Richard Weikart joined the editorial board of the organization."
    },
    "reporting_perspective": {
      "type": "string",
      "description": "The perspective from which the organization reports on science, technology, and society."
    }
  },
  "required": [
    "organization_name",
    "is_non_profit",
    "country_of_origin",
    "year_weikart_joined_board",
    "reporting_perspective"
  ],
  "additionalProperties": false
}
