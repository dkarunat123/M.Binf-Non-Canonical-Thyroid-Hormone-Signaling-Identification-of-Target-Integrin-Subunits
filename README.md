# M.Binf Poster: Identification of Target Integrin Thyroid Hormone Receptors From Sea Urchins

This repository holds files relevant to my Master of Bioinformatics Research Project: Non-Canonical Thyroid Hormone Signaling Identification of Target Integrin Subunits in Metastasis &amp; Development.

## Project Summary

This project investigates the potential for **non-canonical thyroid hormone signaling** in sea urchins through **RGD-binding integrin receptors**.

In humans, thyroid hormone metabolites such as T3 and T4 bind to the integrin **αVβ3**, initiating rapid, transcription-independent signaling. While sea urchins lack a direct ortholog of αVβ3, they express several integrin heterodimers (such as **αVβG**, **αVβ1-A**, and **αVβC**) that may serve analogous functions.

Using **AlphaFold-Multimer**, candidate sea urchin integrins were structurally modeled, followed by **molecular docking** of six thyroid hormone metabolites using **HADDOCK 2.5**. Binding affinities were calculated with **PRODIGY**, and structural comparisons with human αVβ3 were performed.

The results highlight **αVβG** and **αVβ1-A** as promising functional analogs of human αVβ3, based on favorable docking scores and high interface confidence. These findings support a possible conserved mechanism of thyroid hormone interaction in echinoderms, offering insights into the evolution of integrin-mediated signaling.

## Poster References

Ludwig, B. S., Kessler, H., Kossatz, S., & Reuning, U. (2021). RGD-binding integrins revisited: How recently discovered functions and novel synthetic ligands (re-)shape an ever-evolving field. *Cancers, 13*(7), 1711. https://doi.org/10.3390/cancers13071711

Taylor, V. H., Heyland, A., & Brown, D. D. (2014). Thyroid hormone membrane receptor binding and transcriptional regulation in the sea urchin *Strongylocentrotus purpuratus*. *General and Comparative Endocrinology, 205*, 83–89. https://doi.org/10.1016/j.ygcen.2014.05.023

Tieman, K. (in press). *Molecular modeling of αVβ integrins in the sea urchin Strongylocentrotus purpuratus and their potential role in thyroid hormone binding* (Master’s thesis). University of Guelph.

Tobi, D., & Reichman, D. (2023). Three-dimensional modeling of thyroid hormone metabolites binding to the cancer-relevant αvβ3 integrin: In-silico based study. *International Journal of Molecular Sciences, 24*(13), 10711. https://doi.org/10.3390/ijms241310711

Xiong, J.-P., Mahalingham, B., Alonso, J. L., Borrelli, L. A., Rui, X., Anand, S., Hyman, B. T., Rysiok, T., Müller-Pompalla, D., Goodman, S. L., & Arnaout, M. A. (2004). Crystal structure of the extracellular segment of integrin αVβ3 in complex with an Arg-Gly-Asp ligand. *Science, 303*(5663), 1391–1395. https://doi.org/10.1126/science.1092616

### Panel 1 Figures:

**(A)** Created with [BioRender.com](https://biorender.com).  
**(B)** Rendered using **PubChem** and **PyMOL**.  
**(C)** Created using a combination of [BioRender.com](https://biorender.com) and **PyMOL**.  
**(D)** Created with [BioRender.com](https://biorender.com), *adapted from (Ludwig et al., 2021).*  
**(E)** Created by Sarah Locilento (Heyland Lab, University of Guelph) for her *in-progress M.Sc. thesis* (University of Guelph).

### Panel 3 Figures:

**(A)–(G)** Generated using **AlphaFold-Multimer** structural predictions.  
Structures were visualized in **PyMOL** and colored by **pLDDT confidence scores** using a custom Python script.

### Panel 3 (cont’d) Figures:

**(A)–(D)** Docked complexes were generated using **HADDOCK 2.5** and visualized in **PyMOL**.


### Resources and Tools

- **Echinobase**: [https://www.echinobase.org](https://www.echinobase.org) — Sea urchin genome and transcriptome data.
- **NCBI BLASTP**: [https://blast.ncbi.nlm.nih.gov/Blast.cgi](https://blast.ncbi.nlm.nih.gov/Blast.cgi) — Used for protein homology searches.
- **AlphaFold-Multimer**: [https://alphafoldserver.com](https://alphafoldserver.com) — Used for protein structure prediction of integrin dimers.
- **PubChem**: [https://pubchem.ncbi.nlm.nih.gov](https://pubchem.ncbi.nlm.nih.gov) — Source of thyroid hormone metabolite structures.
- **Open Babel (Format Converter)**: [https://www.cheminfo.org/Chemistry/Cheminformatics/FormatConverter/index.html](https://www.cheminfo.org/Chemistry/Cheminformatics/FormatConverter/index.html) — Used to convert ligand files to PDB format.
- **HADDOCK 2.4**: [https://rascar.science.uu.nl/haddock2.4/](https://rascar.science.uu.nl/haddock2.4/) — Protein-ligand docking server for AlphaFold-predicted integrins and thyroid hormones.
- **PRODIGY-LIG**: [https://rascar.science.uu.nl/prodigy/lig](https://rascar.science.uu.nl/prodigy/lig) — Used to obtain ΔG and values from docked complexes.


