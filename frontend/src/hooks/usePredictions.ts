import { useEffect, useState } from "react";
import { api } from "../api/api";
import type { Predictions } from "../types/predictions";

export function usePredictions() {

    const [predictions, setPredictions] = useState<Predictions[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function fetchPredictions() {

            try {

                const response = await api.get("/predictions/");

                console.log("Predictions:", response.data);

                if (Array.isArray(response.data)) {
                    setPredictions(response.data);
                } else {
                    setPredictions([]);
                }

            } catch (error) {

                console.error("Prediction fetch failed:", error);

                setPredictions([]);

            } finally {

                setLoading(false);

            }

        }

        fetchPredictions();

    }, []);

    return {
        predictions,
        loading,
    };
}