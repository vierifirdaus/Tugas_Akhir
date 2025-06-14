// src/lib/api.ts
import { API_BASE_URL } from '@/constants/flowConstants';
import { VisualizeCodePayload, VisualizeCodeResponse, CallGraphResponse } from '@/types';

/**
 * Mengirim kode Python ke backend untuk visualisasi.
 * @param payload - Objek yang berisi kode Python.
 * @returns Promise yang resolve dengan data hasil visualisasi.
 * @throws Error jika terjadi masalah pada API call.
 */
export async function visualizePythonCode(payload: VisualizeCodePayload): Promise<VisualizeCodeResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/method`, { // Asumsi endpoint utama adalah /method
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      let errorMessage = `API Error: ${response.status} ${response.statusText}`;
      try {
        const errorData = await response.json();
        errorMessage = errorData.message || errorData.error || errorMessage;
      } catch (e) { /* Biarkan error message default */ }
      throw new Error(errorMessage);
    }
    return await response.json() as VisualizeCodeResponse;
  } catch (error) {
    console.error("Error fetching visualization data:", error);
    throw error;
  }
}

/**
 * Mengambil data call graph dari backend.
 * @param payload - Objek yang berisi kode Python.
 * @returns Promise yang resolve dengan data call graph.
 * @throws Error jika terjadi masalah pada API call.
 */
export async function fetchCallGraph(payload: VisualizeCodePayload): Promise<CallGraphResponse> {
    try {
        const response = await fetch(`${API_BASE_URL}/call_graph`, {
            method: 'POST', // Asumsi endpoint ini juga POST
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let errorMessage = `Call Graph API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                errorMessage = errorData.message || errorData.error || errorMessage;
            } catch (e) { /* Biarkan error message default */ }
            throw new Error(errorMessage);
        }
        return await response.json() as CallGraphResponse;
    } catch (error) {
        console.error("Error fetching call graph data:", error);
        throw error;
    }
}