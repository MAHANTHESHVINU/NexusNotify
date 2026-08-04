import pandas as pd


class CSVExporter:

    def export(self, predictions, output_path):

        rows = []

        for p in predictions:

            rows.append(
                {
                    "message_id": p.message_id,
                    "action": p.action,
                    "message_type": p.message_type,
                    "reason": p.reason,
                    "confidence": p.confidence,
                    "evidence_message_ids": (
                        ";".join(p.evidence_message_ids)
                        if p.evidence_message_ids
                        else "none"
                    ),
                }
            )

        pd.DataFrame(rows).to_csv(
            output_path,
            index=False,
        )