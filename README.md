# analise_dados

Atividades de Python (análise de dados com pandas, matplotlib, seaborn e Streamlit), 3ª etapa, turma 3A1, COTEMIG 2026.

| Pasta | Atividade |
|-------|-----------|
| `atividade_1` | Atividade 1: vetores, matrizes e Series (mini exercício no final do notebook) |
| `atividade_2` | Atividade 2: indicadores de horas em afazeres domésticos, mulheres x homens (Tabela 1.1.1) |
| `atividade_3` | Atividade 3: formação na graduação dividida em 3 tabelas + `describe` (Tabela 3) |
| `atividade_4` | Atividade 4: população 2010 x 2022 por estado e município, salva em CSV |
| `graficos` | Gráficos: gráficos das atividades 2, 3 e 4 |
| `atividade_5` | Atividade 5: IDH por estado com melt e matplotlib (Tabela 4) |
| `atividade_6` | Atividade 6: merge das Tabelas 5 (2012 x 2026) com a Tabela 1.1.1, melt e gráfico |
| `streamlit_aula1` | Streamlit, primeiros passos: dashboard da padaria |
| `EXEMPLO` | Tabela aula hoje: dashboard Streamlit + Plotly com a Tabela 1.1.2 |

## Como rodar

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_aula1/arquivo.py
python -m streamlit run EXEMPLO/arquivo.py
```

Cada notebook lê as tabelas que estão na própria pasta:

- `atividade_2` e `atividade_6`: `Tabela 1.1.1.xls`
- `atividade_3`: `Tabela_3_Areas_gerais_de_formacao_na_graduacao.xlsx`
- `atividade_4`: `CD2022_Populacao_2010_Compatibilizada_20231222.xlsx`
- `atividade_5`: `Tabela4.csv`
- `atividade_6`: `Tabela5-sem_emprego_2012.csv` e `Tabela5-sem_emprego_2026.csv`
- `EXEMPLO`: `Tabela 1.1.2.xls`
- `graficos`: usa as tabelas das pastas `atividade_2`, `atividade_3` e `atividade_4`

Fonte dos dados: IBGE (PNAD Contínua, Censo Demográfico 2022) e IDHM.
