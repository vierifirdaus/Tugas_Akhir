// src/lib/api.ts
import { API_BASE_URL } from '@/constants/flowConstants';
import { VisualizeCodePayload, VisualizeCodeResponse, CallGraphResponse, AttributesResponse, PDGResponse } from '@/types';

/**
 * Helper function to handle connection errors
 */
function handleConnectionError(error: any): never {
    if (error instanceof TypeError && error.message.includes('Failed to fetch')) {
        console.error("Connection error:", error);
        throw new Error('error connection');
    }
    console.error("API error:", error);
    throw error;
}

/**
 * Mengirim kode Python ke backend untuk visualisasi.
 * @param payload - Objek yang berisi kode Python.
 * @returns Promise yang resolve dengan data hasil visualisasi.
 * @throws Error jika terjadi masalah pada API call.
 */
export async function fetchCFG(payload: VisualizeCodePayload): Promise<VisualizeCodeResponse> {
    try {
        const response = await fetch(`${API_BASE_URL}/method`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let errorMessage = `API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                errorMessage = errorData.message || errorData.error || errorMessage;
            } catch (e) {
                console.log("Error parsing error response:", e);
            }
            throw new Error(errorMessage);
        }
        return await response.json() as VisualizeCodeResponse;
    } catch (error) {
        return handleConnectionError(error);
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
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let errorMessage = `Call Graph API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                errorMessage = errorData.message || errorData.error || errorMessage;
            } catch (e) {
                console.log("Error parsing error response:", e);
            }
            throw new Error(errorMessage);
        }
        return await response.json() as CallGraphResponse;
    } catch (error) {
        return handleConnectionError(error);
    }
}

export async function fetchAttributes(payload: VisualizeCodePayload): Promise<AttributesResponse> {
    try {
        const response = await fetch(`${API_BASE_URL}/attributes`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let errorMessage = `Attributes API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                errorMessage = errorData.message || errorData.error || errorMessage;
            } catch (e) {
                console.log("Error parsing error response:", e);
            }
            throw new Error(errorMessage);
        }
        return await response.json() as AttributesResponse;
    } catch (error) {
        return handleConnectionError(error);
    }
}

export async function fetchPDG(payload: VisualizeCodePayload): Promise<PDGResponse> {
    try {
        const response = await fetch(`${API_BASE_URL}/pdg`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            let errorMessage = `PDG API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                errorMessage = errorData.message || errorData.error || errorMessage;
            } catch (e) {
                console.log("Error parsing error response:", e);
            }
            throw new Error(errorMessage);
        }
        return await response.json() as PDGResponse;
    } catch (error) {
        return handleConnectionError(error);
    }
}